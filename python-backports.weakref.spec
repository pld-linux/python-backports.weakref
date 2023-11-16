#
# Conditional build:
%bcond_with	tests	# unit tests (atexit test fails for me)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (useful for <3.7 only)

Summary:	Backport of new features in Python's weakref module
Summary(pl.UTF-8):	Backport nowej funkcjonalności modułu Pythona weakref
Name:		python-backports.weakref
Version:	1.0.post1
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.weakref/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.weakref/backports.weakref-%{version}.tar.gz
# Source0-md5:	96ae6adc9b299b1f58849b3b1f8577d7
URL:		https://pypi.org/project/backports.weakref/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-backports.test.support
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-backports.test.support
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides backports of new features in Python's weakref
module under the "backports" namespace.

%description -l pl.UTF-8
Ten pakiet zawiera backport nowej funkcjonalności modułu Pythona
weakref, umieszczony w przestrzeni nazw "backports".

%package -n python3-backports.weakref
Summary:	Backport of new features in Python's weakref module
Summary(pl.UTF-8):	Backport nowej funkcjonalności modułu Pythona weakref
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-backports.weakref
This package provides backports of new features in Python's weakref
module under the "backports" namespace.

%description -n python3-backports.weakref -l pl.UTF-8
Ten pakiet zawiera backport nowej funkcjonalności modułu Pythona
weakref, umieszczony w przestrzeni nazw "backports".

%prep
%setup -q -n backports.weakref-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m unittest discover tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# packaged in python-backports
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.py*
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/backports/weakref.py[co]
%{py_sitescriptdir}/backports.weakref-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backports.weakref
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/backports/weakref.py
%{py3_sitescriptdir}/backports/__pycache__/weakref.cpython-*.py[co]
%{py3_sitescriptdir}/backports.weakref-%{version}-py*.egg-info
%endif
