from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estacionamento.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','carro.views.index',name='index'),
    url(r'^carro/$','carro.views.formCadastroCarro',name='carro'),
    url(r'^cliente/$','cliente.views.formCadastroCliente',name='cliente'), 
    url(r'^vaga/$','vaga.views.formCadastroVaga',name='vaga'), 
    url(r'^aluga/$','vaga.views.formCadastroAlugar',name='aluga'),        
                               
                       
)
