
%define		module	pyirclib

Summary:	Python IRC library
Summary(pl.UTF-8):	Moduły Pythona do obsługi IRC
Name:		python-%{module}
Version:	0.4.3
Release:	7
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyirclib/pyirclib-%{version}.tar.gz
# Source0-md5:	b9d60e69314a548dfd7d48da3d540d62
URL:		http://pyirclib.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
pyirclib is a simple yet powerful IRC library written in Python. It's
intended audience are Python developers wanting to write their own IRC
programs.

%description -l pl.UTF-8
pyirclib jest prostą ale potężną biblioteką do obsługi IRC napisaną w
Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO example* *.html
%{py_sitescriptdir}/*.py[co]
