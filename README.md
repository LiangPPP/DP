## Environment Requirements

- Python version must be greater than `3.7.1` and less than `3.11`.

## Step 1: Install `smartnoise-synth`

Open your terminal and enter the following commands:
```
pip install smartnoise-synth
pip install openDP==0.6.2
```

> **Note:** When running `pip install openDP==0.6.2`, you may see an error in red indicating that `smartnoise-synth` requires `openDP` version to be `>= 0.7.0`. However, due to the lack of a specific API required by `smartnoise-synth` in `openDP` versions after `0.7.0`, we choose to install version `0.6.2`.

## Step 2: Clone the Sample Code

Open your terminal and enter the following command:
```
git clone https://github.com/LiangPPP/DP.git
```

## Step 3: Run the Sample Code

Open your terminal and enter the following commands:
```
cd DP
python3 DP.py
```
