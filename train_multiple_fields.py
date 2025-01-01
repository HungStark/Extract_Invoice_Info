import os
import argparse
from invoicenet import FIELDS
from invoicenet.common import trainer
from invoicenet.acp.acp import AttendCopyParse
from invoicenet.acp.data import InvoiceData

def train_field(field, batch_size, steps, data_dir, restore=False, early_stop_steps=0):
    print(f"\n=== Bắt đầu huấn luyện cho trường: {field} ===")
    
    train_data = InvoiceData.create_dataset(
        field=field,
        data_dir=os.path.join(data_dir, 'train/'),
        batch_size=batch_size
    )
    
    val_data = InvoiceData.create_dataset(
        field=field,
        data_dir=os.path.join(data_dir, 'val/'),
        batch_size=batch_size
    )

    trainer.train(
        model=AttendCopyParse(field=field, restore=restore),
        train_data=train_data,
        val_data=val_data,
        total_steps=steps,
        early_stop_steps=early_stop_steps
    )

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fields", type=str, nargs='+', choices=FIELDS.keys(),
                    help="danh sách các trường cần huấn luyện")
    ap.add_argument("--batch_size", type=int, default=3,
                    help="kích thước batch cho huấn luyện")
    ap.add_argument("--restore", action="store_true",
                    help="khôi phục từ checkpoint")
    ap.add_argument("--data_dir", type=str, default='processed_data/',
                    help="đường dẫn đến thư mục chứa dữ liệu đã chuẩn bị")
    ap.add_argument("--steps", type=int, default=400,
                    help="số bước huấn luyện tối đa cho mỗi trường")
    ap.add_argument("--early_stop_steps", type=int, default=0,
                    help="dừng huấn luyện nếu validation không cải thiện sau số bước này")

    args = ap.parse_args()

    for field in args.fields:
        train_field(
            field=field,
            batch_size=args.batch_size,
            steps=args.steps,
            data_dir=args.data_dir,
            restore=args.restore,
            early_stop_steps=args.early_stop_steps
        )

if __name__ == '__main__':
    main() 