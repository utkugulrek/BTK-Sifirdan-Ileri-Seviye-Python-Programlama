"""
https://www.kaggle.com/datasets/datasnaek/youtube-new
GBvideos.csv için çalışmalar
Dosya boyutu büyük olduğu için GitHub'a yüklenmedi.
"""

import pandas as pd

df = pd.read_csv("datasets/GBvideos.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
result = df.drop(
    [
        "thumbnail_link",
        "comments_disabled",
        "ratings_disabled",
        "video_error_or_removed",
        "description",
    ],
    axis=1,
)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df["likes"].mean().round(2)
result = df["dislikes"].mean().round(2)

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["likes", "dislikes"]].head(50)

# 7- En çok görüntülenen video hangisidir ?
result = df.loc[df["views"].idxmax(), ["title", "views"]]

# 8- En düşük görüntülenen video hangisidir?
result = df.loc[df["views"].idxmin(), ["title", "views"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.nlargest(10, "views")[["title", "views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id")["likes"].mean().sort_values().round(2)

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)

# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)
result = df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))
df["tag_count"] = df["tags"].str.count(r"\|") + 1  # daha performanslı
df.loc[df["tags"].isin(["[none]", ""]), "tag_count"] = 0  # etiketsizleri çıkarma
result = df

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
# df["ratio"] = df["likes"] / df["dislikes"]
# df.sort_values(by="ratio", inplace=True, ascending=False)

ratio = df["likes"] / df["dislikes"]
df["like_dislike_ratio"] = ratio.replace([float("inf"), float("-inf")], 0).fillna(0)
result = df.sort_values(by="like_dislike_ratio", ascending=False)[
    ["title", "likes", "dislikes", "like_dislike_ratio"]
]

print(result)
