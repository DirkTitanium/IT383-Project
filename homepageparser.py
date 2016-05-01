import os


def bookmarkParser(web1, web2, web3, web4, web5, web6, web7, let1, let2, let3, let4, let5, let6, let7, color1, color2,
                   color3, color4, color5, color6, color7):
    dir = os.getcwd() + "\Hometab\index.html"
    data = open(dir, "r")
    lines = data.readlines()
    data.close()
    data = open(dir, "w")

    for line in lines:
        if "<!--parser-->" not in line:
            data.write(line)
        else:
            if "<!--bookmark1-->" in line:
                if web1 == "example.com" and let1 == "*" and color1 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark1-->\n')
                else:
                    if "https://" not in web1:
                        web1 = "https://" + web1
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color1 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web1 + '">' + let1 + '</a></div><!--parser--><!--bookmark1-->\n'
                    data.write(bookmark)

            if "<!--bookmark2-->" in line:
                if web2 == "example.com" and let2 == "*" and color2 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark2-->\n')
                else:
                    if "https://" not in web2:
                        web2 = "https://" + web2
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color2 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web2 + '">' + let2 + '</a></div><!--parser--><!--bookmark2-->\n'
                    data.write(bookmark)

            if "<!--bookmark3-->" in line:
                if web3 == "example.com" and let3 == "*" and color3 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark3-->\n')
                else:
                    if "https://" not in web3:
                        web3 = "https://" + web3
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color3 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web3 + '">' + let3 + '</a></div><!--parser--><!--bookmark3-->\n'
                    data.write(bookmark)

            if "<!--bookmark4-->" in line:
                if web4 == "example.com" and let4 == "*" and color4 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark4-->\n')
                else:
                    if "https://" not in web4:
                        web4 = "https://" + web4
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color4 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web4 + '">' + let4 + '</a></div><!--parser--><!--bookmark4-->\n'
                    data.write(bookmark)

            if "<!--bookmark5-->" in line:
                if web5 == "example.com" and let5 == "*" and color5 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark5-->\n')
                else:
                    if "https://" not in web5:
                        web5 = "https://" + web5
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color5 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web5 + '">' + let5 + '</a></div><!--parser--><!--bookmark5-->\n'
                    data.write(bookmark)

            if "<!--bookmark6-->" in line:
                if web6 == "example.com" and let6 == "*" and color6 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark6-->\n')
                else:
                    if "https://" not in web6:
                        web6 = "https://" + web6
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color6 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web6 + '">' + let6 + '</a></div><!--parser--><!--bookmark6-->\n'
                    data.write(bookmark)

            if "<!--bookmark7-->" in line:
                if web7 == "example.com" and let7 == "*" and color7 == "gray":
                    data.write(
                        '           <div class="wcircle-menu-item" style="background-color:#2ecc71;border-radius:50%;padding:15px;width:20px;height:20px;"><a href="https://www.google.com">*</a></div><!--parser--><!--bookmark7-->\n')
                else:
                    if "https://" not in web7:
                        web7 = "https://" + web7
                    bookmark = '            <div class="wcircle-menu-item" style="background-color:' + color7 + ';border-radius:50%;padding:15px;width:20px;height:20px;"><a href="' + web7 + '">' + let7 + '</a></div><!--parser--><!--bookmark7-->\n'
                    data.write(bookmark)


def wallpaperParser(img1, img2, img3, img4, img5, img6):
    dir = os.getcwd() + "\Hometab\css\main.css"
    data = open(dir, "r")
    lines = data.readlines()
    data.close()
    data = open(dir, "w")
    for line in lines:
        if "/*parser*/" not in line:
            data.write(line)
        else:
            if "/*image1*/" in line:
                if img1 == "------------------->":
                    data.write(line)
                else:
                    image = "    /*parser*/  background-image: url('" + img1 + "'); /*image1*/\n"
                    data.write(image)
            if "/*image2*/" in line:
                if img2 == "------------------->":
                    data.write(line)
                else:
                    data.write("    /*parser*/  background-image: url('" + img2 + "'); /*image1*/\n")
            if "/*image3*/" in line:
                if img3 == "------------------->":
                    data.write(line)
                else:
                    data.write("    /*parser*/  background-image: url('" + img3 + "'); /*image1*/\n")
            if "/*image4*/" in line:
                if img4 == "------------------->":
                    data.write(line)
                else:
                    data.write("    /*parser*/  background-image: url('" + img4 + "'); /*image1*/\n")
            if "/*image5*/" in line:
                if img5 == "------------------->":
                    data.write(line)
                else:
                    data.write("    /*parser*/  background-image: url('" + img5 + "'); /*image1*/\n")
            if "/*image6*/" in line:
                if img6 == "------------------->":
                    data.write(line)
                else:
                    data.write("    /*parser*/  background-image: url('" + img6 + "'); /*image1*/\n")

    data.close()
