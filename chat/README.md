### Run Training

**Multi-gpu**

```
TRANSFORMERS_VERBOSITY=info torchrun --nproc_per_node=8 train.py config.yaml --deepspeed=deepspeed_z3_config_bf16.json
```

**Single-gpu single-node**

```
TRANSFORMERS_VERBOSITY=info torchrun \
    --standalone \
    --nproc_per_node=1 \
    train.py config.yaml --deepspeed=deepspeed_z3_config_bf16.json
```

**DeepSpeed**

```
deepspeed --num_gpus=2 your_program.py <normal cl args> --deepspeed ds_config.json
```