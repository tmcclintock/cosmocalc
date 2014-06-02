# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
Cosmology and LSS calculations - python interface to (fast) C code
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cosmocalc', [dirname(__file__)])
        except ImportError:
            import _cosmocalc
            return _cosmocalc
        if fp is not None:
            try:
                _mod = imp.load_module('_cosmocalc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cosmocalc = swig_import_helper()
    del swig_import_helper
else:
    import _cosmocalc
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


RHO_CRIT = _cosmocalc.RHO_CRIT
CSOL = _cosmocalc.CSOL
DELTAC = _cosmocalc.DELTAC
DH = _cosmocalc.DH
TCMB = _cosmocalc.TCMB
class cosmocalcData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cosmocalcData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cosmocalcData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cosmoNum"] = _cosmocalc.cosmocalcData_cosmoNum_set
    __swig_getmethods__["cosmoNum"] = _cosmocalc.cosmocalcData_cosmoNum_get
    if _newclass:cosmoNum = _swig_property(_cosmocalc.cosmocalcData_cosmoNum_get, _cosmocalc.cosmocalcData_cosmoNum_set)
    __swig_setmethods__["OmegaM"] = _cosmocalc.cosmocalcData_OmegaM_set
    __swig_getmethods__["OmegaM"] = _cosmocalc.cosmocalcData_OmegaM_get
    if _newclass:OmegaM = _swig_property(_cosmocalc.cosmocalcData_OmegaM_get, _cosmocalc.cosmocalcData_OmegaM_set)
    __swig_setmethods__["OmegaB"] = _cosmocalc.cosmocalcData_OmegaB_set
    __swig_getmethods__["OmegaB"] = _cosmocalc.cosmocalcData_OmegaB_get
    if _newclass:OmegaB = _swig_property(_cosmocalc.cosmocalcData_OmegaB_get, _cosmocalc.cosmocalcData_OmegaB_set)
    __swig_setmethods__["OmegaL"] = _cosmocalc.cosmocalcData_OmegaL_set
    __swig_getmethods__["OmegaL"] = _cosmocalc.cosmocalcData_OmegaL_get
    if _newclass:OmegaL = _swig_property(_cosmocalc.cosmocalcData_OmegaL_get, _cosmocalc.cosmocalcData_OmegaL_set)
    __swig_setmethods__["OmegaK"] = _cosmocalc.cosmocalcData_OmegaK_set
    __swig_getmethods__["OmegaK"] = _cosmocalc.cosmocalcData_OmegaK_get
    if _newclass:OmegaK = _swig_property(_cosmocalc.cosmocalcData_OmegaK_get, _cosmocalc.cosmocalcData_OmegaK_set)
    __swig_setmethods__["OmegaNu"] = _cosmocalc.cosmocalcData_OmegaNu_set
    __swig_getmethods__["OmegaNu"] = _cosmocalc.cosmocalcData_OmegaNu_get
    if _newclass:OmegaNu = _swig_property(_cosmocalc.cosmocalcData_OmegaNu_get, _cosmocalc.cosmocalcData_OmegaNu_set)
    __swig_setmethods__["h"] = _cosmocalc.cosmocalcData_h_set
    __swig_getmethods__["h"] = _cosmocalc.cosmocalcData_h_get
    if _newclass:h = _swig_property(_cosmocalc.cosmocalcData_h_get, _cosmocalc.cosmocalcData_h_set)
    __swig_setmethods__["Sigma8"] = _cosmocalc.cosmocalcData_Sigma8_set
    __swig_getmethods__["Sigma8"] = _cosmocalc.cosmocalcData_Sigma8_get
    if _newclass:Sigma8 = _swig_property(_cosmocalc.cosmocalcData_Sigma8_get, _cosmocalc.cosmocalcData_Sigma8_set)
    __swig_setmethods__["As"] = _cosmocalc.cosmocalcData_As_set
    __swig_getmethods__["As"] = _cosmocalc.cosmocalcData_As_get
    if _newclass:As = _swig_property(_cosmocalc.cosmocalcData_As_get, _cosmocalc.cosmocalcData_As_set)
    __swig_setmethods__["As_pivot"] = _cosmocalc.cosmocalcData_As_pivot_set
    __swig_getmethods__["As_pivot"] = _cosmocalc.cosmocalcData_As_pivot_get
    if _newclass:As_pivot = _swig_property(_cosmocalc.cosmocalcData_As_pivot_get, _cosmocalc.cosmocalcData_As_pivot_set)
    __swig_setmethods__["SpectralIndex"] = _cosmocalc.cosmocalcData_SpectralIndex_set
    __swig_getmethods__["SpectralIndex"] = _cosmocalc.cosmocalcData_SpectralIndex_get
    if _newclass:SpectralIndex = _swig_property(_cosmocalc.cosmocalcData_SpectralIndex_get, _cosmocalc.cosmocalcData_SpectralIndex_set)
    __swig_setmethods__["delta"] = _cosmocalc.cosmocalcData_delta_set
    __swig_getmethods__["delta"] = _cosmocalc.cosmocalcData_delta_get
    if _newclass:delta = _swig_property(_cosmocalc.cosmocalcData_delta_get, _cosmocalc.cosmocalcData_delta_set)
    __swig_setmethods__["w0"] = _cosmocalc.cosmocalcData_w0_set
    __swig_getmethods__["w0"] = _cosmocalc.cosmocalcData_w0_get
    if _newclass:w0 = _swig_property(_cosmocalc.cosmocalcData_w0_get, _cosmocalc.cosmocalcData_w0_set)
    __swig_setmethods__["wa"] = _cosmocalc.cosmocalcData_wa_set
    __swig_getmethods__["wa"] = _cosmocalc.cosmocalcData_wa_get
    if _newclass:wa = _swig_property(_cosmocalc.cosmocalcData_wa_get, _cosmocalc.cosmocalcData_wa_set)
    __swig_setmethods__["useSmoothTransFunc"] = _cosmocalc.cosmocalcData_useSmoothTransFunc_set
    __swig_getmethods__["useSmoothTransFunc"] = _cosmocalc.cosmocalcData_useSmoothTransFunc_get
    if _newclass:useSmoothTransFunc = _swig_property(_cosmocalc.cosmocalcData_useSmoothTransFunc_get, _cosmocalc.cosmocalcData_useSmoothTransFunc_set)
    def __init__(self): 
        this = _cosmocalc.new_cosmocalcData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cosmocalc.delete_cosmocalcData
    __del__ = lambda self : None;
cosmocalcData_swigregister = _cosmocalc.cosmocalcData_swigregister
cosmocalcData_swigregister(cosmocalcData)


def turn_off_gsl_errs():
  """turn off GSL error handling"""
  return _cosmocalc.turn_off_gsl_errs()

def angdist(*args):
  """angular diameter distance in Mpc/h - angdist(scale factor)"""
  return _cosmocalc.angdist(*args)

def lumdist(*args):
  """luminosity distance in Mpc/h - lumdist(scale factor)"""
  return _cosmocalc.lumdist(*args)

def comvdist(*args):
  """comoving distance in Mpc/h - comvdist(scale factor)"""
  return _cosmocalc.comvdist(*args)

def angdistdiff(*args):
  """angular diatameter distance difference in Mpc/h for lensing - angdistdiff(amin,amax) [amin <= amax]"""
  return _cosmocalc.angdistdiff(*args)

def acomvdist(*args):
  """scale factor for a given comoving distance in Mpc/h - acomvdist(comv. dist in Mpc/h)"""
  return _cosmocalc.acomvdist(*args)

def comvdist_exact(*args):
  """comoving distance in Mpc/h - comvdist_exact(scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.comvdist_exact(*args)

def transfer_function(*args):
  """EH98 transfer function - transfer_function(k in h/Mpc) [uses spline]"""
  return _cosmocalc.transfer_function(*args)

def transfunct_eh98(*args):
  """EH98 transfer function - transfunct_eh98(k in h/Mpc) [evaluates fitting formula - slower than transfer_function]"""
  return _cosmocalc.transfunct_eh98(*args)

def transfunct_eh98_smooth(*args):
  """EH98 transfer function w/ no BAO wiggles - transfunct_eh98_smooth(k in h/Mpc)"""
  return _cosmocalc.transfunct_eh98_smooth(*args)

def linear_powspec(*args):
  """linear power spectrum P(k) - linear_powspec(k in h/Mpc, scale factor)"""
  return _cosmocalc.linear_powspec(*args)

def linear_powspec_exact(*args):
  """linear power spectrum P(k) - linear_powspec_exact(k in h/Mpc, scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.linear_powspec_exact(*args)

def convert_cmbnorm2sigma8():
  """convert CMB power spectrum amplitude to sigma8 - convert_cmbnorm2sigma8()"""
  return _cosmocalc.convert_cmbnorm2sigma8()

def linear_corrfunc_exact(*args):
  """linear corr. function xi(r) - linear_corrfunc(r in Mpc/h, scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.linear_corrfunc_exact(*args)

def linear_corrfunc(*args):
  """linear corr. function xi(r) - linear_corrfunc(r in Mpc/h, scale factor)"""
  return _cosmocalc.linear_corrfunc(*args)

def nonlinear_powspec(*args):
  """Takahashi+12 HaloFit nonlinear power spectrum - nonlinear_powspec(k in h/Mpc, scale factor)"""
  return _cosmocalc.nonlinear_powspec(*args)

def nonlinear_corrfunc_exact(*args):
  """Takahashi+12 HaloFit nonlinear corr. function xi(r) - nonlinear_corrfunc(r in Mpc/h, scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.nonlinear_corrfunc_exact(*args)

def nonlinear_corrfunc(*args):
  """Takahashi+12 HaloFit nonlinear corr. function xi(r) - nonlinear_corrfunc(r in Mpc/h, scale factor)"""
  return _cosmocalc.nonlinear_corrfunc(*args)

def growth_function_exact(*args):
  """growth function ODE integration - growth_function_exact(scale factor) [does ODE as opposed to using spline]"""
  return _cosmocalc.growth_function_exact(*args)

def growth_function(*args):
  """growth function ODE integration - growth_function(scale factor)"""
  return _cosmocalc.growth_function(*args)

def growth_function_exact_nonorm(*args):
  """growth function ODE integration w/ no normalization - growth_function_exact_nonorm(scale factor) [does ODE as opposed to using spline]"""
  return _cosmocalc.growth_function_exact_nonorm(*args)

def weff(*args):
  """effective w for DE so that rho_{DE} = Omega_{DE}(a=1)/a^(3*(1+weff(a))) - weff(scale factor)"""
  return _cosmocalc.weff(*args)

def hubble_noscale(*args):
  """hubble function H(a)/H0 - hubble_noscale(scale factor)"""
  return _cosmocalc.hubble_noscale(*args)

def sigmaRtophat_exact(*args):
  """RMS variance in top hat sphere of radius R of linear power spectrum - sigmaRtophat(radius in Mpc/h, scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.sigmaRtophat_exact(*args)

def sigmaRtophat(*args):
  """RMS variance in top hat sphere of radius R of linear power spectrum - sigmaRtophat(radius in Mpc/h, scale factor)"""
  return _cosmocalc.sigmaRtophat(*args)

def sigmaMtophat_exact(*args):
  """RMS variance for mass M of linear power spectrum - sigmaMtophat(mass in M_{sun}/h, scale factor) [does integration as opposed to using spline]"""
  return _cosmocalc.sigmaMtophat_exact(*args)

def sigmaMtophat(*args):
  """RMS variance for mass M of linear power spectrum - sigmaMtophat(mass in M_{sun}/h, scale factor)"""
  return _cosmocalc.sigmaMtophat(*args)

def inverse_sigmaRtophat(*args):
  """sphere of radius R given RMS variance in linear power spectrum - inverse_sigmaRtophat(RMS variance sigma(R,scale factor), scale factor)"""
  return _cosmocalc.inverse_sigmaRtophat(*args)

def inverse_sigmaMtophat(*args):
  """mass M given RMS variance in linear power spectrum - inverse_sigmaMtophat(RMS variance sigma(M,scale factor), scale factor)"""
  return _cosmocalc.inverse_sigmaMtophat(*args)

def tinker2008_mass_function(*args):
  """Tinker+08 mass function - tinker2008_mass_function(mass, scale factor, delta w/ mean density)"""
  return _cosmocalc.tinker2008_mass_function(*args)

def tinker2010_mass_function(*args):
  """Tinker+10 mass function - tinker2010_mass_function(mass, scale factor, delta w/ mean density)"""
  return _cosmocalc.tinker2010_mass_function(*args)

def tinker2010_bias(*args):
  """Tinker+10 halos bias - tinker2010_bias(mass, scale factor, delta w/ mean density)"""
  return _cosmocalc.tinker2010_bias(*args)
_cosmocalc.cvar.cosmoData.cosmoNum = 1
_cosmocalc.turn_off_gsl_errs()

def _init(cd):
    _cosmocalc.cvar.cosmoData.cosmoNum += 1
    _cosmocalc.cvar.cosmoData.OmegaM  = _cosmodict_resolve(cd,'om')
    _cosmocalc.cvar.cosmoData.OmegaL  = _cosmodict_resolve(cd,'ol')
    _cosmocalc.cvar.cosmoData.OmegaB  = _cosmodict_resolve(cd,'ob')
    okval = _cosmodict_resolve(cd,'ok')
    if okval is None:
        _cosmocalc.cvar.cosmoData.OmegaK = 1.0 - _cosmocalc.cvar.cosmoData.OmegaM - _cosmocalc.cvar.cosmoData.OmegaL
    else:
        _cosmocalc.cvar.cosmoData.OmegaK = okval
    _cosmocalc.cvar.cosmoData.h = _cosmodict_resolve(cd,'h')
    _cosmocalc.cvar.cosmoData.SpectralIndex = _cosmodict_resolve(cd,'ns')

    _cosmocalc.cvar.cosmoData.w0 = -1.0
    _cosmocalc.cvar.cosmoData.wa = 0.0
    if _cosmodict_resolve(cd,'w') is not None:
        _cosmocalc.cvar.cosmoData.w0 = _cosmodict_resolve(cd,'w')
        _cosmocalc.cvar.cosmoData.wa = 0.0
    elif _cosmodict_resolve(cd,'w0') is not None and _cosmodict_resolve(cd,'wa') is not None:
        _cosmocalc.cvar.cosmoData.w0 = _cosmodict_resolve(cd,'w0')
        _cosmocalc.cvar.cosmoData.wa = _cosmodict_resolve(cd,'wa')

    asval = _cosmodict_resolve(cd,'as')
    as_pivot_val = _cosmodict_resolve(cd,'as_pivot')
    s8val = _cosmodict_resolve(cd,'s8')
    if asval is not None and as_pivot_val is not None and s8val is None:
        _cosmocalc.cvar.cosmoData.As = asval
        _cosmocalc.cvar.cosmoData.As_pivot = as_pivot_val
	_cosmocalc.cvar.cosmoData.Sigma8 = _cosmocalc.convert_cmbnorm2sigma8()
    elif s8val is not None:
        _cosmocalc.cvar.cosmoData.Sigma8 = s8val

def _cosmodict_resolve(cd,skey,keynames=None):
    _keynames = [
        ['omega_m','om','OmegaM','Omega_M','omegam'],
        ['omega_l','ol','OmegaL','Omega_L','omegal',
         'omega_de','ode','OmegaDE','Omega_DE','omegade'],
        ['omega_k','ok','OmegaK','Omega_K','omegak'],
        ['omega_r','or','OmegaR','Omega_R','omegar'],
        ['omega_nu','onu','OmegaNu','Omega_Nu','omeganu',
         'OmegaNU','Omega_NU'],
        ['omega_b','ob','OmegaB','Omega_B','omegab'],
        ['H0'],
        ['h','hubble'],
        ['s8','sigma8','Sigma8','sigma_8','Sigma_8'],
        ['as','As'],
	['as_pivot','As_pivot','AsPivot','as_Pivot','As_Pivot'],
        ['ns','SpectralIndex','spectral_index','spectralindex'],
        ['w','W'],
        ['w0','W0'],
        ['wa','wA','WA']
        ]
    if keynames is None:
        keynames = _keynames
    for keylist in keynames:
        if skey in keylist:
            for tkey in keylist:
                if tkey in cd:
                    return cd[tkey]
    return None

def set_cosmology(cd):
    """Set the cosmology using a dictionary like this

           import cosmocalc
           cd = {
               "OmegaM":0.3,
               "OmegaB":0.045,
               "OmegaDE":0.7,
               "OmegaK":0.0,
               "h":0.7,
               "Sigma8":0.8,
               "SpectralIndex":0.95,
               "w0":-1.0,
               "wa":0.0
               "As":2.1e-9,
               "As_pivot":0.05}
           cosmocalc.set_cosmology(cd)
       
       Note that the cosmology is set *globally*, so you can only use 1 at a time!
       """
    _init(cd)

def get_cosmology():
    "Return the cosmology as a dictionary. See cosmocalc.set_cosmology() for an example."
    return {'OmegaM':_cosmocalc.cvar.cosmoData.OmegaM,
            'OmegaDE':_cosmocalc.cvar.cosmoData.OmegaL,
            'OmegaB':_cosmocalc.cvar.cosmoData.OmegaB,
            'OmegaK':_cosmocalc.cvar.cosmoData.OmegaK,
            'h':_cosmocalc.cvar.cosmoData.h,
            'Sigma8':_cosmocalc.cvar.cosmoData.Sigma8,
            'SpectralIndex':_cosmocalc.cvar.cosmoData.SpectralIndex,
            'w0':_cosmocalc.cvar.cosmoData.w0,
            'wa':_cosmocalc.cvar.cosmoData.wa}

def lcdm():
    "Return a random cosmology."
    return {'OmegaM':0.3,'OmegaDE':0.7,'OmegaB':0.045,'OmegaK':0.0,'h':0.7,'Sigma8':0.8,'SpectralIndex':0.95,'w0':-1.0,'wa':0.0}


# This file is compatible with both classic and new-style classes.

cvar = _cosmocalc.cvar

