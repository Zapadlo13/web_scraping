from yattag import Doc


def create(columns, data):
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('head'):
            with tag('link', href='css/index.css', rel='stylesheet'):
                pass

        with tag('body'):
            with tag('table', klass='table_sort'):
                with tag('thead'):
                    with tag('tr'):
                        for column in columns:
                            with tag('th'):
                                text(column)

                with tag('tbody'):
                    for line in data:
                        with tag('tr'):
                            for column in columns:
                                with tag('td'):
                                    text(line.get(column))
                    pass
            with tag('script', src="js/sort.js"):
                pass
            result = doc.getvalue()
            return result
