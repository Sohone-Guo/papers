```python
source_input_hiddens.permute(1, 0, 2)
```

```python
copy_probabilities = self._scatter(
	encoder_input, output_len,
	torch.zeros_like(output_probabilities),
	attn_weights)

output_probabilities.scatter_add_(2, text_n_gram_index.unsqueeze(1),
								  text_n_gram_value.unsqueeze(1))
```