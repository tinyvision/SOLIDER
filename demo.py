from swin_transformer import swin_tiny_patch4_window7_224,swin_small_patch4_window7_224,swin_base_patch4_window7_224

model_path = './log/lup/swin_small/checkpoint.pth'
semantic_weight = 1.0

swin = swin_small_patch4_window7_224(convert_weights=False, semantic_weight=semantic_weight)
swin.init_weights(model_path)
feat_dim = swin.num_features[-1]
print(feat_dim)
