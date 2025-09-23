#!/usr/bin/env python3

print("Starting debug test...")

try:
    print("Testing dataset import...")
    from dataset import datasets
    print(f"Dataset sizes available: {list(datasets.keys())}")
    print("Dataset import successful")
except Exception as e:
    print(f"Dataset import error: {e}")

try:
    print("Testing lab1_ciii import...")
    from lab1_ciii import find_optimal_s
    print("lab1_ciii import successful")
except Exception as e:
    print(f"lab1_ciii import error: {e}")

try:
    print("Testing hybridsort import...")
    from hybridsort import hybrid_mergesort, pure_mergesort
    print("hybridsort import successful")
except Exception as e:
    print(f"hybridsort import error: {e}")

print("Debug test completed")
