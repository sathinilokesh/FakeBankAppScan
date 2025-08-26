from datasets import load_dataset
import pandas as pd
import os
from typing import List, Optional

def load_lamda_data(years: List[int] = [2023, 2024, 2025], 
                    split: str = 'train', 
                    nsamples_per_year: Optional[int] = None,
                    save_path: str = './data/processed/lamda_subset.csv') -> pd.DataFrame:
    """
    Load LAMDA dataset for specified years and split.
    
    Args:
        years: List of years to load (e.g., [2023, 2024, 2025])
        split: Dataset split ('train', 'test', 'val')
        nsamples_per_year: Optional limit on samples per year
        save_path: Path to save the combined CSV file
        
    Returns:
        Combined pandas DataFrame with all loaded samples
    """
    try:
        # Load the full dataset
        dataset = load_dataset("IQSeC-Lab/LAMDA","Baseline")
        all_data = []
        
        print(f"Available splits in dataset: {list(dataset.keys())}")
        
        for year in years:
            split_key = f'{year}_{split}'
            
            if split_key not in dataset:
                print(f"Warning: Split '{split_key}' not found in dataset. Skipping...")
                continue
                
            year_data = dataset[split_key]
            print(f"Loading {len(year_data)} samples from {split_key}")
            
            # Optionally limit samples per year
            if nsamples_per_year and len(year_data) > nsamples_per_year:
                year_data = year_data.select(range(nsamples_per_year))
                print(f"Limited to {nsamples_per_year} samples for {year}")
            
            # Convert to DataFrame
            df = pd.DataFrame(year_data)
            df['source_year'] = year  # Add year column for tracking
            df['source_split'] = split  # Add split column for tracking
            all_data.append(df)
        
        if not all_data:
            print("No data was loaded. Please check the year and split parameters.")
            return pd.DataFrame()
        
        # Combine all DataFrames
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save to CSV
        combined_df.to_csv(save_path, index=False)
        
        print(f"\nSuccessfully loaded {len(combined_df)} samples from years {years}")
        print(f"Data saved to: {save_path}")
        print(f"Dataset shape: {combined_df.shape}")
        print(f"Columns: {list(combined_df.columns)}")
        
        # Show basic statistics
        if 'label' in combined_df.columns:
            print(f"\nLabel distribution:")
            print(combined_df['label'].value_counts())
            
        return combined_df
        
    except Exception as e:
        print(f"Error loading LAMDA dataset: {str(e)}")
        print("Make sure you have the 'datasets' package installed: pip install datasets")
        return pd.DataFrame()

def explore_lamda_structure():
    """
    Explore the structure of LAMDA dataset to understand available splits and features.
    """
    try:
        dataset = load_dataset("IQSeC-Lab/LAMDA","Baseline")

        print("LAMDA Dataset Structure:")
        print(f"Available splits: {list(dataset.keys())}")
        
        # Show sample from first available split
        first_split = list(dataset.keys())[0]
        sample = dataset[first_split][0]
        
        print(f"\nSample from {first_split}:")
        for key, value in sample.items():
            print(f"  {key}: {type(value)} - {str(value)[:100]}...")
            
    except Exception as e:
        print(f"Error exploring dataset: {str(e)}")

# Example usage with error handling
if __name__ == "__main__":
    # First explore the dataset structure
    print("Exploring LAMDA dataset structure...")
    explore_lamda_structure()
    
    print("\n" + "="*50 + "\n")
    
    # Load specific years with limited samples for testing
    df = load_lamda_data(
        years=[2024, 2025], 
        split='train', 
        nsamples_per_year=1000,  # Limit for faster loading during testing
        save_path='data/processed/lamda_banking_subset.csv'
    )
    
    if not df.empty:
        print("\nFirst 5 rows:")
        print(df.head())
        
        print("\nDataset info:")
        print(df.info())
