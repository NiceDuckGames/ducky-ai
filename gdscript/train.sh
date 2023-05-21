#!/bin/bash

cd santacoder-finetuning/
pip install -r requirements.txt

hu

RESUME=0
if [ ! -z "$2" ]; then
    $RESUME=1
fi

NGPU=1
if [ ! -z "$1" ]; then
    $NGPU=$1
fi
    
python -m torch.distributed.run \
    --nproc_per_node=$1 train.py \
    --model_path="bigcode/santacoder" \
    --dataset_name="bigcode/the-stack-dedup" \
    --subset="data/gdscript" \
    --data_column "content" \
    --split="train" \
    --seq_length=2048 \
    --max_steps=1000 \
    --batch_size=2 \
    --gradient_accumulation_steps 4 \
    --learning_rate=5e-5 \
    --num_warmup_steps=100 \
    --eval_freq=100 \
    --save_freq=100 \
    --log_freq=1 \
    --resume=$RESUME \
    --num_workers="$(nproc)" \
    --no_fp16
