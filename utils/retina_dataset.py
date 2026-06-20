from torch.utils.data import Dataset
import cv2
import os

class RetinaDataset(Dataset):

    def __init__(self, dataframe, image_dir, transform=None):

        self.df = dataframe
        self.image_dir = image_dir
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        #temporary debugging code
        image_path = os.path.join(
        self.image_dir,
        image_name + ".jpg")

        print(image_path)

        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(
                f"Failed to load: {image_path}"
            )
        


        
        image_name = self.df.iloc[idx]["Image name"]

        label = self.df.iloc[idx]["Retinopathy grade"]

        image_path = os.path.join(
            self.image_dir,
            image_name + ".jpg"
        )

        print(image_path)

        image = cv2.imread(image_path)

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        if self.transform:

            image = self.transform(
                image=image
            )["image"]

        return image, label
    
        
        
        