import sys
import os
import json
import pandas as pd
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_potential_failures():
    """Test for potential failure points in the main pipeline"""
    print("Testing potential failure points...")
    
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Test 1: Songs loading
    try:
        with open(os.path.join(script_dir, "data", "songs.json"), "r") as f:
            songs = json.load(f)[:10]
        print(f" Songs loading: {len(songs)} songs")
    except Exception as e:
        print(f" Songs loading failed: {e}")
        return False
    
    # Test 2: Data_Fetcher initialization
    try:
        from DJ.api import Data_Fetcher
        data_fetcher = Data_Fetcher()
        print(" Data_Fetcher initialization")
    except Exception as e:
        print(f" Data_Fetcher initialization failed: {e}")
        return False
    
    # Test 3: PreProcessor initialization
    try:
        from DJ.preprocessor import PreProcessor
        processor = PreProcessor()
        print(" PreProcessor initialization")
    except Exception as e:
        print(f" PreProcessor initialization failed: {e}")
        return False
    
    # Test 4: QwenAPI initialization (with mock key)
    try:
        from DJ.api import QwenAPI
        with patch.dict(os.environ, {'qwen_key': 'test_key'}):
            qwen = QwenAPI()
        print(" QwenAPI initialization")
    except Exception as e:
        print(f" QwenAPI initialization failed: {e}")
        return False
    
    # Test 5: File path construction
    try:
        for song in songs[:3]:
            mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
            # Just test path construction, not file existence
            assert isinstance(mp3_path, str)
        print(" File path construction")
    except Exception as e:
        print(f" File path construction failed: {e}")
        return False
    
    # Test 6: Feature extraction (if MP3 exists)
    mp3_found = False
    for song in songs[:3]:
        mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
        if os.path.exists(mp3_path):
            try:
                features = processor.extract_features(mp3_path)
                assert isinstance(features, dict)
                assert len(features) > 0
                print(f" Feature extraction on {song['name']}")
                mp3_found = True
                break
            except Exception as e:
                print(f" Feature extraction failed on {song['name']}: {e}")
                return False
    
    if not mp3_found:
        print("  No MP3 files found for feature extraction test")
    
    # Test 7: DataFrame creation
    try:
        test_data = [{
            'id': 1,
            'name': 'Test',
            'artist': 'Test',
            'qwen_analysis': 'Test',
            'tempo_bpm': 120.0
        }]
        df = pd.DataFrame(test_data)
        assert len(df) == 1
        print(" DataFrame creation")
    except Exception as e:
        print(f" DataFrame creation failed: {e}")
        return False
    
    # Test 8: CSV saving
    try:
        test_csv = "test_failure_check.csv"
        df.to_csv(test_csv, index=False)
        assert os.path.exists(test_csv)
        os.remove(test_csv)  # Clean up
        print(" CSV saving")
    except Exception as e:
        print(f" CSV saving failed: {e}")
        return False
    
    print("\n All failure point tests passed!")
    return True

def test_mock_pipeline():
    """Test the complete pipeline with mocked Qwen calls"""
    print("\n🔍 Testing complete pipeline with mocks...")
    
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load songs
    with open(os.path.join(script_dir, "data", "songs.json"), "r") as f:
        songs = json.load(f)[:2]  # Just 2 songs for testing
    
    from DJ.preprocessor import PreProcessor
    from DJ.api import Data_Fetcher
    
    # Initialize
    data_fetcher = Data_Fetcher()
    processor = PreProcessor()
    
    # Mock Qwen calls
    with patch.object(processor.qwen, 'upload_temp_mp3') as mock_upload, \
         patch.object(processor.qwen, 'call_qwen') as mock_call:
        
        mock_upload.return_value = "https://test-url.com/test.mp3"
        mock_call.return_value = ("Mock analysis result", None)
        
        for song in songs:
            mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
            
            if not os.path.exists(mp3_path):
                print(f"     Skipping {song['name']} - no MP3 file")
                continue
            
            print(f"   Processing: {song['name']}")
            
            # Extract features
            features = processor.extract_features(mp3_path)
            
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
    
    # Test final DataFrame
    if processor.df_data:
        df = pd.DataFrame(processor.df_data)
        print(f" Created DataFrame: {df.shape}")
        print(f"   Columns: {list(df.columns)[:10]}...")
    else:
        print("  No data processed (no MP3 files found)")
    
    print(" Mock pipeline test completed!")

if __name__ == "__main__":
    if test_potential_failures():
        test_mock_pipeline()
