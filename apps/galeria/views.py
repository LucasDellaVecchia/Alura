from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario nao logado!")
        return redirect("login")
    
    fotografias = Fotografia.objects.order_by("data_publica").filter(publica=True)
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario nao logado!")
        return redirect("login")
    
    fotografias = Fotografia.objects.order_by("data_publica").filter(publica=True)

    if "buscar" in request.GET:
        nome_busca = request.GET["buscar"]
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)

    return render(request, "galeria/index.html", {"cards": fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario nao esta logado!")
        return redirect("login")
    
    form = FotografiaForms

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem registrada com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Preencha corretamente as informacoes da imagem!")
            return redirect("nova_imagem")

    return render(request, "galeria/nova_imagem.html", {"form": form})


def alterar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem Alterada com sucesso!")
            return redirect("index")

    return render(request, "galeria/alterar_imagem.html", {"form": form, "foto_id": foto_id})


def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Imagem deletada com sucesso!")
    return redirect("index")


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_publica").filter(publica=True, categoria=categoria)
    return render(request, "galeria/index.html", {"cards": fotografias})