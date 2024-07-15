Tags: #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
![[Pasted image 20240715215253.png]]

```python
class LoRALinear(nn.Module):
    """
    Implementation of:
        - LoRA: https://arxiv.org/abs/2106.09685

    Notes:
        - Freezing is handled at network level, not layer level.
        - Scaling factor controls relative importance of LoRA skip
          connection versus original frozen weight. General guidance is
          to keep it to 2.0 and sweep over learning rate when changing
          the rank.
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        rank: int,
        scaling: float,
        bias: bool = False,
    ):
        super().__init__()

        self.in_features = in_features
        self.out_features = out_features
        assert not bias
        self.bias = bias
        self.rank = rank
        self.scaling = scaling

        self.lora_A = nn.Linear(
            self.in_features,
            self.rank,
            bias=self.bias,
        )
        self.lora_B = nn.Linear(
            self.rank,
            self.out_features,
            bias=self.bias,
        )

        self.linear = nn.Linear(self.in_features, self.out_features, bias=self.bias)

        # make sure no LoRA weights are marked as "missing" in load_state_dict
        def ignore_missing_keys(m: nn.Module, incompatible_keys: NamedTuple):
            incompatible_keys.missing_keys[:] = []  # type: ignore

        self.register_load_state_dict_post_hook(ignore_missing_keys)

    def forward(self, x: torch.Tensor):
        lora = self.lora_B(self.lora_A(x))
        return self.linear(x) + lora * self.scaling

    def _load_from_state_dict(self, state_dict, prefix, *args, **kwargs):
        key_name = prefix + "weight"

        # full checkpoint
        if key_name in state_dict:
            w_ref = state_dict[key_name]

            # load frozen weights
            state_dict = {
                "linear.weight": w_ref,
                "lora_A.weight": torch.zeros_like(
                    self.lora_A.weight, device=w_ref.device, dtype=w_ref.dtype
                ),
                "lora_B.weight": torch.zeros_like(
                    self.lora_B.weight, device=w_ref.device, dtype=w_ref.dtype
                ),
            }
            self.load_state_dict(state_dict, assign=True, strict=True)
```

# Question
---


# Reference
---


# Attachment
---
![[lora.pdf]]