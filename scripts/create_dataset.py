import os
import shutil
from fire import Fire


def create_dataset(path_to_dataset: str = "./mel-spectrogram") -> None:
    """
    Creates a dataset directory structure for mel-spectrogram data.

    Args:
        main_path (str, optional): The main directory path where the dataset folders will be created. Defaults to "./mel-spectrogram".

    Returns:
        None
    """
    train_path = os.path.join(path_to_dataset, "train")
    test_path = os.path.join(path_to_dataset, "test")
    if not os.path.exists(train_path):
        os.mkdir(train_path)
        os.mkdir(os.path.join(train_path, "True"))
        os.mkdir(os.path.join(train_path, "Noise"))
        os.mkdir(os.path.join(train_path, "Pink"))
    if not os.path.exists(test_path):
        os.mkdir(test_path)
        os.mkdir(os.path.join(test_path, "True"))
        os.mkdir(os.path.join(test_path, "Noise"))
        os.mkdir(os.path.join(test_path, "Pink"))

    folders = os.listdir(path_to_dataset)
    folders.remove("train")
    folders.remove("test")
    for index, folder in enumerate(folders):
        if index == 0:
            path_to_folder = os.path.join(path_to_dataset, folder)
            for sub_folder in os.listdir(path_to_folder):
                sub_folder_path = os.path.join(path_to_folder, sub_folder)
                copy_path = os.path.join(test_path, sub_folder)
                shutil.copytree(sub_folder_path, copy_path, dirs_exist_ok=True)

        else:
            path_to_folder = os.path.join(path_to_dataset, folder)
            for sub_folder in os.listdir(path_to_folder):
                sub_folder_path = os.path.join(path_to_folder, sub_folder)
                copy_path = os.path.join(train_path, sub_folder)
                try:
                    shutil.copytree(sub_folder_path, copy_path, dirs_exist_ok=True)
                except:
                    continue


if __name__ == "__main__":
    Fire(create_dataset)
