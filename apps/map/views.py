from django.shortcuts import render
import folium

def mapa_view(request):
    # Coordenadas de Xanxerê, SC
    latitude = -26.8933
    longitude = -52.4097

    # Criar o mapa centrado em Xanxerê
    mapa = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], popup='Xanxerê').add_to(mapa)


    folium.Marker(
    location=[-26.8756, -52.4061],
    popup='Instituição Genérica - Centro de Xanxerê',
    icon=folium.Icon(color='green')
    ).add_to(mapa)

    folium.Marker(
    location=[-26.8700, -52.3901],
    popup='Instituição Genérica 2 - Centro de Xanxerê',
    icon=folium.Icon(color='black')
    ).add_to(mapa)


    folium.Marker(
    location=[-26.8600, -52.4101],
    popup='Instituição Genérica 3 - Centro de Xanxerê',
    icon=folium.Icon(color='pink')
    ).add_to(mapa)

    # Transformar o mapa em HTML
    mapa_html = mapa._repr_html_()  # Obtém o HTML do mapa para uso direto no template

    # Renderizar a página passando o HTML do mapa
    return render(request, 'apps/map/map.html', {'mapa_html': mapa_html})



from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import CompraForm
from .models import Compra, Instituicao

def fazer_doacao(request):
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mapa')
    else:
        form = CompraForm()
    
    # Adicionando as instituições ao contexto
    instituicoes = Instituicao.objects.all()
    return render(request, 'apps/map/map.html', {'form': form, 'CompraForm': CompraForm})


# View para listar as doações realizadas pelo usuário
def suas_doacoes(request):
    doacoes = Compra.objects.filter(usuario=request.user)  # Filtra por usuário logado
    filtro = request.GET.get('filtro')

    return render(request, 'apps/map/map.html')
