from django.db import models


# class Tempat(models.Model):
#     nama = models.CharField(max_length=50)
#     alamat = models.TextField()

#     def __str__(self) -> str:
#         return self.nama

class Kategori(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nama


class Fasilitas(models.Model):
    nama = models.CharField(max_length=50)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nama


class Pertanyaan(models.Model):
    text = models.TextField()
    # tempat = models.ForeignKey(Tempat, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.text


class Respon(models.Model):
    text = models.TextField()
    pertanyaan = models.ForeignKey(
        Pertanyaan, on_delete=models.CASCADE, null=True)
    # tempat = models.ForeignKey(Tempat, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.text
# Create your models here.
