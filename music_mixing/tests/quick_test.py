import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def quick_test():
    """Quick test to catch obvious issues"""
    print("Quick validation test...")
    
    # Test 1: Check songs.json
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    songs_path = os.path.join(script_dir, "data", "songs.json")
    
    if not os.path.exists(songs_path):
        print("songs.json not found!")
        return False
    
    with open(songs_path, "r") as f:
        songs = json.load(f)
    
    print(f"Found {len(songs)} songs")
    
    # Test 2: Check imports
    try:
        from DJ.preprocessor import PreProcessor
        from DJ.api import Data_Fetcher, QwenAPI
        print("All imports successful")
    except ImportError as e:
        print(f"Import error: {e}")
        return False
    
    # Test 3: Check if we have any MP3s
    mp3_count = 0
    for song in songs[:5]:  # Check first 5
        mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
        if os.path.exists(mp3_path):
            mp3_count += 1
    
    if mp3_count == 0:
        print("No MP3 files found - will need to download first")
    else:
        print(f"Found {mp3_count} MP3 files")
    
    # Test 4: Check environment variables
    import os
    if not os.getenv("qwen_key"):
        print("qwen_key not set - Qwen API calls will fail")
    else:
        print("qwen_key is set")
    
    # Test 5: Test feature extraction on first available MP3
    if mp3_count > 0:
        try:
            processor = PreProcessor()
            for song in songs[:5]:
                mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
                if os.path.exists(mp3_path):
                    print(f"   Testing feature extraction on: {song['name']}")
                    features = processor.extract_features(mp3_path)
                    print(f"   Extracted {len(features)} features")
                    break
        except Exception as e:
            print(f"Feature extraction failed: {e}")
            return False

    print("\nQuick test completed!")
    return True

if __name__ == "__main__":
    quick_test()
