import os
from tkFileDialog import *
from Tkinter import *
from tkMessageBox import *
import homepageparser


class HomepageEdit:
    def __init__(self, master):
        self.frame = master

        # ----- Frames -----#
        leftSide = Frame(self.frame, bd=4, relief=SUNKEN, height=250)
        leftSide.grid(row=0, column=0)
        rightSide = Frame(self.frame, bd=4, relief=SUNKEN, bg="grey", height=250)
        rightSide.grid(row=0, column=1)

        # ----- Save button -----#
        Button(self.frame, text="Save", command=self.save).grid(row=1, column=1)

        # ----- Images -----#
        Label(rightSide, text="BackGround Images").grid(row=0, column=1)
        Button(rightSide, text="?", command=self.helpWallpaper).grid(row=0, column=2)

        # ----- 1st Background -----#
        Label(rightSide, text="1st Wallpaper").grid(row=1, column=0)
        self.image1 = Entry(rightSide)
        self.image1.grid(row=1, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation1).grid(row=1, column=2)
        self.image1.delete(0, END)
        self.image1.insert(0, "------------------->")

        # ----- 2nd Background -----#
        Label(rightSide, text="2nd Wallpaper").grid(row=2, column=0)
        self.image2 = Entry(rightSide)
        self.image2.grid(row=2, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation2).grid(row=2, column=2)
        self.image2.delete(0, END)
        self.image2.insert(0, "------------------->")

        # ----- 3rd Background -----#
        Label(rightSide, text="3rd Wallpaper").grid(row=3, column=0)
        self.image3 = Entry(rightSide)
        self.image3.grid(row=3, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation3).grid(row=3, column=2)
        self.image3.delete(0, END)
        self.image3.insert(0, "------------------->")

        # ----- 4th Background -----#
        Label(rightSide, text="4th Wallpaper").grid(row=4, column=0)
        self.image4 = Entry(rightSide)
        self.image4.grid(row=4, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation4).grid(row=4, column=2)
        self.image4.delete(0, END)
        self.image4.insert(0, "------------------->")

        # ----- 5th Background -----#
        Label(rightSide, text="5th Wallpaper").grid(row=5, column=0)
        self.image5 = Entry(rightSide)
        self.image5.grid(row=5, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation5).grid(row=5, column=2)
        self.image5.delete(0, END)
        self.image5.insert(0, "------------------->")

        # ----- 6th Background -----#
        Label(rightSide, text="6th Wallpaper").grid(row=6, column=0)
        self.image6 = Entry(rightSide)
        self.image6.grid(row=6, column=1)
        Button(rightSide, text="Pick an Image", command=self.imageLocation6).grid(row=6, column=2)
        self.image6.delete(0, END)
        self.image6.insert(0, "------------------->")

        # ----- Bookmarks -----#
        Label(leftSide, text="Type in a bookmark").grid(row=0)
        Button(leftSide, text="?", command=self.helpBookmark).grid(row=0, column=1)

        # ----- 1st Bookmark -----#
        Label(leftSide, text="1st Bookmark").grid(row=1, columnspan=2, sticky=E + W)
        self.bm1 = Entry(leftSide)
        self.bm1.grid(row=2, columnspan=2, sticky=E + W)
        self.bm1.delete(0, END)
        self.bm1.insert(0, "example.com")

        self.l1 = Entry(leftSide, width=2)
        self.l1.grid(row=3)
        self.l1.delete(0, END)
        self.l1.insert(0, "*")

        self.color1 = Entry(leftSide)
        self.color1.grid(row=3, column=1)
        self.color1.delete(0, END)
        self.color1.insert(0, "gray")

        # ----- 2nd Bookmark -----#
        Label(leftSide, text="2nd Bookmark").grid(row=5, columnspan=2, sticky=E + W)
        self.bm2 = Entry(leftSide)
        self.bm2.grid(row=6, columnspan=2, sticky=E + W)
        self.bm2.delete(0, END)
        self.bm2.insert(0, "example.com")

        self.l2 = Entry(leftSide, width=2)
        self.l2.grid(row=7)
        self.l2.delete(0, END)
        self.l2.insert(0, "*")

        self.color2 = Entry(leftSide)
        self.color2.grid(row=7, column=1)
        self.color2.delete(0, END)
        self.color2.insert(0, "gray")

        # ----- 3rd Bookmark -----#
        Label(leftSide, text="3rd Bookmark").grid(row=9, columnspan=2, sticky=E + W)
        self.bm3 = Entry(leftSide)
        self.bm3.grid(row=10, columnspan=2, sticky=E + W)
        self.bm3.delete(0, END)
        self.bm3.insert(0, "example.com")

        self.l3 = Entry(leftSide, width=2)
        self.l3.grid(row=11)
        self.l3.delete(0, END)
        self.l3.insert(0, "*")

        self.color3 = Entry(leftSide)
        self.color3.grid(row=11, column=1)
        self.color3.delete(0, END)
        self.color3.insert(0, "gray")

        # ----- 4th Bookmark -----#
        Label(leftSide, text="4th Bookmark").grid(row=13, columnspan=2, sticky=E + W)
        self.bm4 = Entry(leftSide)
        self.bm4.grid(row=14, columnspan=2, sticky=E + W)
        self.bm4.delete(0, END)
        self.bm4.insert(0, "example.com")

        self.l4 = Entry(leftSide, width=2)
        self.l4.grid(row=15)
        self.l4.delete(0, END)
        self.l4.insert(0, "*")

        self.color4 = Entry(leftSide)
        self.color4.grid(row=15, column=1)
        self.color4.delete(0, END)
        self.color4.insert(0, "gray")

        # ----- 5th Bookmark -----#
        Label(leftSide, text="5th Bookmark").grid(row=17, columnspan=2, sticky=E + W)
        self.bm5 = Entry(leftSide)
        self.bm5.grid(row=18, columnspan=2, sticky=E + W)
        self.bm5.delete(0, END)
        self.bm5.insert(0, "example.com")

        self.l5 = Entry(leftSide, width=2)
        self.l5.grid(row=19)
        self.l5.delete(0, END)
        self.l5.insert(0, "*")

        self.color5 = Entry(leftSide)
        self.color5.grid(row=19, column=1)
        self.color5.delete(0, END)
        self.color5.insert(0, "gray")

        # ----- 6th Bookmark -----#
        Label(leftSide, text="6th Bookmark").grid(row=21, columnspan=2, sticky=E + W)
        self.bm6 = Entry(leftSide)
        self.bm6.grid(row=22, columnspan=2, sticky=E + W)
        self.bm6.delete(0, END)
        self.bm6.insert(0, "example.com")

        self.l6 = Entry(leftSide, width=2)
        self.l6.grid(row=23)
        self.l6.delete(0, END)
        self.l6.insert(0, "*")

        self.color6 = Entry(leftSide)
        self.color6.grid(row=23, column=1)
        self.color6.delete(0, END)
        self.color6.insert(0, "gray")

        # ----- 7th Bookmark -----#
        Label(leftSide, text="7th Bookmark").grid(row=25, columnspan=2, sticky=E + W)
        self.bm7 = Entry(leftSide)
        self.bm7.grid(row=26, columnspan=2, sticky=E + W)
        self.bm7.delete(0, END)
        self.bm7.insert(0, "example.com")

        self.l7 = Entry(leftSide, width=2)
        self.l7.grid(row=27)
        self.l7.delete(0, END)
        self.l7.insert(0, "*")

        self.color7 = Entry(leftSide)
        self.color7.grid(row=27, column=1)
        self.color7.delete(0, END)
        self.color7.insert(0, "gray")

    # ----- Image Locations -----#

    def imageLocation1(self):
        filename = askopenfilename()
        print filename
        self.image1.delete(0, END)
        self.image1.insert(0, str(filename))

    def imageLocation2(self):
        filename = askopenfilename()
        self.image2.delete(0, END)
        self.image2.insert(0, str(filename))

    def imageLocation3(self):
        filename = askopenfilename()
        self.image3.delete(0, END)
        self.image3.insert(0, str(filename))

    def imageLocation4(self):
        filename = askopenfilename()
        self.image4.delete(0, END)
        self.image4.insert(0, str(filename))

    def imageLocation5(self):
        filename = askopenfilename()
        self.image5.delete(0, END)
        self.image5.insert(0, str(filename))

    def imageLocation6(self):
        filename = askopenfilename()
        self.image6.delete(0, END)
        self.image6.insert(0, str(filename))

    # ----- Save function -----#

    def save(self):
        bm1 = self.bm1.get()
        bm2 = self.bm2.get()
        bm3 = self.bm3.get()
        bm4 = self.bm4.get()
        bm5 = self.bm5.get()
        bm6 = self.bm6.get()
        bm7 = self.bm7.get()
        let1 = self.l1.get()
        let2 = self.l2.get()
        let3 = self.l3.get()
        let4 = self.l4.get()
        let5 = self.l5.get()
        let6 = self.l6.get()
        let7 = self.l7.get()
        color1 = self.color1.get()
        color2 = self.color2.get()
        color3 = self.color3.get()
        color4 = self.color4.get()
        color5 = self.color5.get()
        color6 = self.color6.get()
        color7 = self.color7.get()
        image1 = self.image1.get()
        image2 = self.image2.get()
        image3 = self.image3.get()
        image4 = self.image4.get()
        image5 = self.image5.get()
        image6 = self.image6.get()
        lettercounter = 0
        imagecounter = 0
        letters = [let1, let2, let3, let4, let5, let6, let7]
        images = [image1, image2, image3, image4, image5, image6]
        formats = ["png", "jpeg", "jpg", "bmp"]

        for x in letters:
            lettercounter += 1
            if len(x) < 1 or len(x) > 1:
                showerror("Bookmark" + str(lettercounter) + "Error", "Must be a single letter or asterisk!")
                return

        for image in images:
            lettercounter += 1
            if "------------------->" not in image:
                newimage = image.split(".")
                if newimage[1] not in formats:                        
                    showerror("Wallpaper{0}error".format(str(imagecounter)), 'Must be a supported image file')
                    return
                else: continue
            else: continue

        homepageparser.wallpaperParser(image1, image2, image3, image4, image5, image6)
        homepageparser.bookmarkParser(bm1, bm2, bm3, bm4, bm5, bm6, bm7, let1, let2, let3, let4, let5, let6, let7,
                                      color1, color2, color3, color4, color5, color6, color7)
        showinfo("Success!", "Your Homepage has been edited!")
        path = os.getcwd()+"\hometab\index.html"

        os.startfile(path)

    def helpWallpaper(self):
        path = os.getcwd() + "\helpWallpaper.pptx"
        os.startfile(path)

    def helpBookmark(self):
        path = os.getcwd() + "\helpBookmarks.pptx"
        os.startfile(path)

    '''
    def colorWindow(self):
        colorWin = Toplevel(root)
        colorWin.title("Pick a Color")
        newWin = ColorSlider(colorWin)

        def getColor():
            self.myColor = newWin.setNew
            colorWin.destroy()
            return self.myColor

        Button(colorWin, text="Make your own color!", command=getColor).grid(row=6)
    '''


root = Tk()
root.title("HomepageEditor")
app = HomepageEdit(root)
root.mainloop()
