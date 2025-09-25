import sys
import os
import json
import pandas as pd
import numpy as np
import librosa
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DJ.preprocessor import PreProcessor
from DJ.api import Data_Fetcher, QwenAPI

def test_environment_setup():
    """Test that all required files and dependencies exist"""
    print(" Testing environment setup...")
    
    # Check if songs.json exists
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    songs_path = os.path.join(script_dir, "data", "songs.json")
    assert os.path.exists(songs_path), f"Songs file not found: {songs_path}"
    
    # Load and validate songs structure
    with open(songs_path, "r") as f:
        songs = json.load(f)
    
    assert isinstance(songs, list), "Songs should be a list"
    assert len(songs) > 0, "Songs list should not be empty"
    
    # Check song structure
    for song in songs[:3]:  # Check first 3 songs
        assert "id" in song, "Song missing 'id' field"
        assert "name" in song, "Song missing 'name' field"
        assert "artist" in song, "Song missing 'artist' field"
        assert isinstance(song["id"], int), "Song ID should be integer"
        assert isinstance(song["name"], str), "Song name should be string"
        assert isinstance(song["artist"], str), "Song artist should be string"
    
    print(" Environment setup test passed")
    return songs

def test_data_fetcher():
    """Test Data_Fetcher class functionality"""
    print(" Testing Data_Fetcher...")
    
    data_fetcher = Data_Fetcher()
    
    # Test get_songs method
    songs = data_fetcher.get_songs()
    assert isinstance(songs, list), "get_songs should return a list"
    assert len(songs) > 0, "Should have songs loaded"
    
    # Test song structure
    song = songs[0]
    assert all(key in song for key in ["id", "name", "artist"]), "Song missing required fields"
    
    print(" Data_Fetcher test passed")
    return songs

def test_preprocessor_initialization():
    """Test PreProcessor class initialization"""
    print(" Testing PreProcessor initialization...")
    
    processor = PreProcessor()
    assert hasattr(processor, 'songs'), "PreProcessor should have songs attribute"
    assert hasattr(processor, 'qwen'), "PreProcessor should have qwen attribute"
    assert hasattr(processor, 'df_data'), "PreProcessor should have df_data attribute"
    assert isinstance(processor.df_data, list), "df_data should be a list"
    
    print(" PreProcessor initialization test passed")

def test_feature_extraction():
    """Test feature extraction on a sample audio file"""
    print(" Testing feature extraction...")
    
    # Create a test audio file (sine wave)
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_audio_path = os.path.join(script_dir, "data", "test_audio.mp3")
    
    # Generate test audio if it doesn't exist
    if not os.path.exists(test_audio_path):
        print("   Creating test audio file...")
        sr = 22050
        duration = 10  # 10 seconds
        t = np.linspace(0, duration, int(sr * duration))
        # Create a simple sine wave
        y = 0.5 * np.sin(2 * np.pi * 440 * t)  # 440 Hz tone
        # Save as MP3 using librosa
        import soundfile as sf
        sf.write(test_audio_path, y, sr)
    
    processor = PreProcessor()
    
    try:
        features = processor.extract_features(test_audio_path)
        
        # Check that features were extracted
        assert isinstance(features, dict), "Features should be a dictionary"
        assert len(features) > 0, "Should have extracted features"
        
        # Check for expected feature keys
        expected_keys = [
            "duration_sec", "tempo_bpm", "tempo_first5_bpm", "tempo_last5_bpm",
            "n_beats", "centroid_mean", "rolloff_mean", "zcr_mean"
        ]
        
        for key in expected_keys:
            assert key in features, f"Missing expected feature: {key}"
        
        # Check data types
        assert isinstance(features["duration_sec"], (int, float)), "Duration should be numeric"
        assert isinstance(features["tempo_bpm"], (int, float)), "Tempo should be numeric"
        assert features["duration_sec"] > 0, "Duration should be positive"
        
        print(f"    Extracted {len(features)} features")
        print(" Feature extraction test passed")
        
    except Exception as e:
        print(f" Feature extraction failed: {e}")
        raise
    
    finally:
        # Clean up test file
        if os.path.exists(test_audio_path):
            os.remove(test_audio_path)

def test_qwen_api_initialization():
    """Test QwenAPI initialization (without making actual calls)"""
    print(" Testing QwenAPI initialization...")
    
    try:
        # Mock the environment variable
        with patch.dict(os.environ, {'qwen_key': 'test_key'}):
            qwen = QwenAPI()
            assert hasattr(qwen, 'client'), "QwenAPI should have client attribute"
            print(" QwenAPI initialization test passed")
    except Exception as e:
        print(f" QwenAPI initialization failed: {e}")
        print("   Make sure qwen_key is set in environment variables")
        raise

def test_file_paths():
    """Test that all file paths are correctly constructed"""
    print(" Testing file path construction...")
    
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Test songs.json path
    songs_path = os.path.join(script_dir, "data", "songs.json")
    assert os.path.exists(songs_path), f"Songs file not found: {songs_path}"
    
    # Test data directory exists
    data_dir = os.path.join(script_dir, "data")
    assert os.path.exists(data_dir), f"Data directory not found: {data_dir}"
    assert os.path.isdir(data_dir), "Data should be a directory"
    
    print(" File paths test passed")

def test_data_processing_flow():
    """Test the complete data processing flow (without Qwen calls)"""
    print(" Testing data processing flow...")
    
    # Load songs
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(script_dir, "data", "songs.json"), "r") as f:
        songs = json.load(f)[:2]  # Test with first 2 songs only
    
    processor = PreProcessor()
    
    # Mock the Qwen API calls
    with patch.object(processor.qwen, 'upload_temp_mp3') as mock_upload, \
         patch.object(processor.qwen, 'call_qwen') as mock_call:
        
        # Set up mocks
        mock_upload.return_value = "https://test-url.com/test.mp3"
        mock_call.return_value = ("Test analysis result", None)
        
        for song in songs:
            mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
            
            # Skip if MP3 doesn't exist (we're not downloading in tests)
            if not os.path.exists(mp3_path):
                print(f"     Skipping {song['name']} - MP3 not found")
                continue
            
            print(f"   Processing: {song['name']}")
            
            # Extract features
            features = processor.extract_features(mp3_path)
            assert isinstance(features, dict), "Features should be dictionary"
            
            # Mock upload and call
            url = processor.qwen.upload_temp_mp3(mp3_path)
            qwen_result, _ = processor.qwen.call_qwen(url)
            
            # Combine data
            row = {
                'id': song['id'],
                'name': song['name'],
                'artist': song['artist'],
                'qwen_analysis': qwen_result,
                **features
            }
            processor.df_data.append(row)
    
    # Test DataFrame creation
    if processor.df_data:
        df = pd.DataFrame(processor.df_data)
        assert len(df) > 0, "DataFrame should have data"
        assert 'qwen_analysis' in df.columns, "DataFrame should have qwen_analysis column"
        print(f"    Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
    
    print(" Data processing flow test passed")

def test_csv_saving():
    """Test CSV saving functionality"""
    print(" Testing CSV saving...")
    
    # Create test data
    test_data = [
        {
            'id': 1,
            'name': 'Test Song',
            'artist': 'Test Artist',
            'qwen_analysis': 'Test analysis',
            'tempo_bpm': 120.0,
            'duration_sec': 180.0
        }
    ]
    
    processor = PreProcessor()
    processor.df_data = test_data
    
    # Test CSV saving
    test_csv_path = "test_output.csv"
    try:
        processor.save_to_csv(test_csv_path)
        assert os.path.exists(test_csv_path), "CSV file should be created"
        
        # Verify CSV content
        df = pd.read_csv(test_csv_path)
        assert len(df) == 1, "CSV should have 1 row"
        assert 'qwen_analysis' in df.columns, "CSV should have qwen_analysis column"
        
        print(" CSV saving test passed")
        
    finally:
        # Clean up
        if os.path.exists(test_csv_path):
            os.remove(test_csv_path)

def run_all_tests():
    """Run all tests"""
    print("🧪 Running comprehensive pipeline tests...")
    print("=" * 50)
    
    try:
        test_environment_setup()
        test_data_fetcher()
        test_preprocessor_initialization()
        test_feature_extraction()
        test_qwen_api_initialization()
        test_file_paths()
        test_data_processing_flow()
        test_csv_saving()
        
        print("\n All tests passed! Pipeline is ready to run.")
        print(" Safe to run main.py")
        
    except Exception as e:
        print(f"\n Test failed: {e}")
        print("🔧 Fix the issues before running main.py")
        raise

if __name__ == "__main__":
    run_all_tests()
