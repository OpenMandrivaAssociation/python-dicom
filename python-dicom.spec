%define module	dicom
%define name	python-%{module}
%define vrsn	0.9.4
%define ptchlvl	1
%define release	%mkrel 2

Summary:	Read, modify and write DICOM files with python code
Name:		%{name}
Version:	%{vrsn}.%{ptchlvl}
Release:	%{release}
Source0:	http://pydicom.googlecode.com/files/pydicom-0.9.4-1.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pydicom.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
%py_requires -d

%description
pydicom is a pure python package for working with DICOM files. It was made
for inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file. As a pure python package,
it should run anywhere python runs without any other requirements.

%prep
%setup -q -n py%{module}-%{vrsn}-%{ptchlvl}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
