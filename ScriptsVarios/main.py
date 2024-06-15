from ScriptsVarios import Data_Cleaning


def main():
    print("Hello, World!")
    root_path_origen = r"C:\Users\crisb\Documents\Trabajo\DataBases\Raw Info\cedulas_2"
    target_path_filter = r"C:\Users\crisb\Documents\Trabajo\DataBases\Raw Info\Filter"
    target_image_path = r"C:\Users\crisb\Documents\Trabajo\DataBases\Raw Info\Images_Filter"
    target_image_path_Original = r"C:\Users\crisb\Documents\Trabajo\DataBases\Raw Info\Images_Filter_Original"
    number_files_filter = 400

    #Data_Cleaning.copy_files(root_path_origen, target_path_filter, number_files_filter)
    #Data_Cleaning.separte_pages(r"C:\Users\crisb\Documents\Trabajo\DataBases\Raw Info\Filter\0.pdf")
    Data_Cleaning.transform_PDF_Image(target_path_filter, target_image_path_Original)

if __name__ == '__main__':
    main()
