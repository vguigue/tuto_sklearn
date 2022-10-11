import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def toto(): # pour jouer avec les modules
    print("coucou")
  
def plot_svm(X, Y, classifier, step=30):
    """ 
        affiche la frontière de décision associée au classifieur
    """
    mmax=X.max(0)
    mmin=X.min(0)
    x1grid,x2grid=np.meshgrid(np.linspace(mmin[0],mmax[0],step),np.linspace(mmin[1],mmax[1],step))
    grid=np.hstack((x1grid.reshape(x1grid.size,1),x2grid.reshape(x2grid.size,1)))
    
    # calcul de la prediction pour chaque point de la grille
    res=classifier.decision_function(grid)
    res=res.reshape(x1grid.shape)
    ax = plt.gca()
    CS = ax.contour(x1grid,x2grid,res,levels=[-1,0,1], colors=(['m','k','m'])) # avec un svm 
    ax.clabel(CS, inline=True, fontsize=10)

# ------------------------ 


def plot_frontiere(X, Y, classifier, step=30, biais=0):
    """ desc_set * label_set * Classifier * int -> NoneType
        Remarque: le 4e argument est optionnel et donne la "résolution" du tracé
        affiche la frontière de décision associée au classifieur
    """
    mmax=X.max(0)
    mmin=X.min(0)
    x1grid,x2grid=np.meshgrid(np.linspace(mmin[0],mmax[0],step),np.linspace(mmin[1],mmax[1],step))
    grid=np.hstack((x1grid.reshape(x1grid.size,1),x2grid.reshape(x2grid.size,1)))
    
    # tracer des frontieres
    if biais == 0:
        # calcul de la prediction pour chaque point de la grille
        res=classifier.predict(grid) 
        res=res.reshape(x1grid.shape)
        plt.contourf(x1grid,x2grid,res,colors=["darksalmon","skyblue"],levels=[-1000,0,1000])    
    else:
        # calcul de la prediction pour chaque point de la grille
        res=classifier.decision_function(grid) + biais
        res=res.reshape(x1grid.shape)
        plt.contour(x1grid,x2grid,res,levels=[0]) # avec un svm 

# ------------------------ 


def plot_mesh(X, Y, classifier, step=30):
    """ desc_set * label_set * Classifier * int -> NoneType
        Remarque: le 4e argument est optionnel et donne la "résolution" du tracé
        affiche la frontière de décision associée au classifieur
    """
    mmax=X.max(0)
    mmin=X.min(0)
    x1grid,x2grid=np.meshgrid(np.linspace(mmin[0],mmax[0],step),np.linspace(mmin[1],mmax[1],step))
    grid=np.hstack((x1grid.reshape(x1grid.size,1),x2grid.reshape(x2grid.size,1)))
    
    # tracer des frontieres
    figax = plt.gca() # récupération des axes axtuels

    # calcul de la prediction pour chaque point de la grille
    res=classifier.decision_function(grid) 
    res=res.reshape(x1grid.shape)

    Z = (res-res.min())/(res.max()-res.min())
    colors = cm.viridis(Z)
    rcount, ccount, _ = colors.shape
    surf = figax.plot_surface(x1grid, x2grid, res,  rcount=rcount, ccount=ccount,
                       facecolors=colors, shade=False)
    surf.set_facecolor((0,0,0,0))
    
# ------------------------ 