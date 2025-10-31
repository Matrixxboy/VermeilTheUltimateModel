# Attention Research Literature Review

This document provides a curated list of seminal papers on attention mechanisms and Transformer models. These papers are essential reading for anyone working on the Vermeil project, as they form the foundation of modern AI.

## Attention and Transformer Papers

| Paper                                                        | Year | Contribution                                                                                                                                                           | Link                                                                |
| :----------------------------------------------------------- | :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| **Neural Machine Translation by Jointly Learning to Align and Translate** | 2014 | Introduced the concept of an attention mechanism in the context of neural machine translation, allowing the model to selectively focus on different parts of the source. | [https://arxiv.org/abs/1409.0473](https://arxiv.org/abs/1409.0473)     |
| **Attention Is All You Need**                                | 2017 | Introduced the Transformer architecture, which is based entirely on attention mechanisms and does away with recurrence and convolutions.                               | [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)     |
| **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** | 2018 | Introduced BERT, a pre-trained language model based on the Transformer architecture that can be fine-tuned for a wide range of downstream tasks.                     | [https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)     |
| **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale** | 2020 | Applied the Transformer architecture to image recognition by treating an image as a sequence of patches (Vision Transformer or ViT).                               | [https://arxiv.org/abs/2010.11929](https://arxiv.org/abs/2010.11929)    |
| **Longformer: The Long-Document Transformer**                | 2020 | Addressed the quadratic complexity of self-attention to efficiently process long documents by using a combination of local and global attention.                  | [https://arxiv.org/abs/2004.05150](https://arxiv.org/abs/2004.05150)     |
| **FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness** | 2022 | A novel attention algorithm that is much faster and more memory-efficient than the standard implementation by using tiling and recomputation.                      | [https://arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135)    |


## Further Reading Resources

| Resource                                | Description                                                                                                                              | Link                                                                    |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| **The Annotated Transformer**           | A detailed explanation of the Transformer architecture with PyTorch code.                                                                | [http://nlp.seas.harvard.edu/2018/04/03/attention.html](http://nlp.seas.harvard.edu/2018/04/03/attention.html) |
| **Hugging Face Transformers**           | The documentation for the popular Transformers library, which provides implementations of many state-of-the-art models.                  | [https://huggingface.co/docs/transformers/index](https://huggingface.co/docs/transformers/index)         |
| **Papers with Code**                    | A great resource for finding the latest papers and code in NLP and other areas of AI.                                                    | [https://paperswithcode.com/area/natural-language-processing](https://paperswithcode.com/area/natural-language-processing) |