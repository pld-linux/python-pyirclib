%include	/usr/lib/rpm/macros.python
%define		module	pyirclib
Summary:	Python IRC library
Summary(pl):	Modu�y Pythona do obs�ugi IRC
Name:		python-%{module}
Version:	0.4.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://prdownloads.sourceforge.net/pyirclib/pyirclib-%{version}.tar.gz
URL:		http://pyirclib.sourceforge.net/
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%requires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
pyirclib is a simple yet powerful IRC library written in Python. It's
intended audience are Python developers wanting to write their own IRC
programs.

%description -l pl
pyirclib jest prost� ale pot�n� bibliotek� do obs�ugi IRC napisan� w
Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 \
        --root=$RPM_BUILD_ROOT

gzip -9nf Changelog README TODO example*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%{py_sitedir}/*.py[co]
