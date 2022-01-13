import fitz # 安装 pymupdf 库
import os
import win32com.client

def word_pdf(Address):
    word = win32com.client.Dispatch('Word.Application')
    for dirpath, dirnames, filenames in os.walk(Address):
        # 判断有没有文件
        if filenames==[]:
            print("文件夹为空，请检查！")
        # 判断是不是含有.doc或者.docx文件
        elif ".doc" or ".docx" in filenames:
            for f in filenames:
                if f.lower().endswith(".docx"):
                    new_name = f.replace(".docx", ".pdf")
                    in_file =(dirpath + '/'+ f)
                    new_file =(dirpath + '/' + new_name)
                    doc = word.Documents.Open(in_file)
                    doc.SaveAs(new_file, FileFormat = 17)
                    print("完成.docx到.pdf的转换！")
                    doc.Close()
                elif f.lower().endswith(".doc"):
                    new_name = f.replace(".doc", ".pdf")
                    in_file =(dirpath +'/' + f)
                    new_file =(dirpath +'/' + new_name)
                    doc = word.Documents.Open(in_file)
                    doc.SaveAs(new_file, FileFormat = 17)
                    print("完成.doc到.pdf的转换！")
                    doc.Close()
    word.Quit()

def pdf_png(Address):
    pdf_dir = []
    os.chdir(Address)
    # 找pdf文件
    docunames = os.listdir()
    if docunames == False:
        print("无文件")
    for docuname in docunames:
        if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
            pdf_dir.append(docuname)
    # 转换成图片
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        print("此文件一共",doc.pageCount,"页...")
        pdf_name = os.path.splitext(pdf)[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG('%s' % pdf_name+str(pg)+str(".png"))
            print("完成第"+str(pg)+str("页的转换..."))
        print("完成全部.pdf到.png的转换！")

if __name__ == '__main__':
    Address = input("请输入需要转换的文件所在文件夹地址：") # 输入文件地址
    word_pdf(Address) # word文档转pdf文档
    pdf_png(Address) # pdf文档转png图片