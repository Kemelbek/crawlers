def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    header = _gettext(page.xpath('.//header/h1/text()'))
    author = _gettext(page.xpath('.//footer/div[3]/div/div[1]//text()'))
    text = _gettext(page.xpath('.//article/div[3]/div[2]//text()[1]'))

    article_data = {
        "url": response.url,
        "header": header,
        "author": author,
        "text": text
    }

    if article_data["text"] is not None:
        # If 'rule' is not set, it defaults to 'pass', which triggers the
        # final 'store' stage.
        context.emit(data=article_data)

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
