from donut import DonutModel
from PIL import Image
import torch
model = DonutModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
if torch.cuda.is_available():
    model.half()
    device = torch.device("cuda")
    model.to(device)
else:
    model.encoder.to(torch.float)
model.eval()
# inputs, labels = inputs.to(device), labels.to(device)
image = Image.open("D:\Python_Project\ocr_donut\donut\misc\sample_image_cord_test_receipt_00004.png").convert("RGB")
# image = Image.open("./donut/misc/sample_image_cord_test_receipt_00004.png").convert("RGB")
output = model.inference(image=image, prompt="<s_cord-v2>")
output