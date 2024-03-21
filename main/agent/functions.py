import fitz

from ..models import UploadedFile


def get_all_files_context(user):
    files = UploadedFile.objects.filter(user=user)
    text = ""

    for file in files:
        try:
            text += "\n\n\n\n\n\nDocument name: " + file.file.name
            doc = fitz.open(file.file.name)
            page_num = 1
            for page in doc:
                text += f"\n Page: {page_num} \n"
                text += page.get_text()
                page_num += 1
            doc.close()
        except Exception as e:
            print(e)
    print(text)
    return text