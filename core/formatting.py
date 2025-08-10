def as_table(rows, headers):
    cols = [headers] + rows
    widths = [max(len(str(row[i])) for row in cols) for i in range(len(headers))]

    def fmt(row):
        return " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers)))

    sep = "-+-".join("-" * w for w in widths)
    return "<pre>" + "\n".join([fmt(headers), sep] + [fmt(r) for r in rows]) + "</pre>"
