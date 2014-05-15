%define module	dicom
%define vrsn	0.9.4
%define ptchlvl	1

Summary:	Read, modify and write DICOM files with python code

Name:		python-%{module}
Version:	0.9.8
Release:	%mkrel 2
Source0:	http://pydicom.googlecode.com/files/pydicom-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pydicom.googlecode.com/
BuildArch:	noarch
BuildRequires:  python-devel

%description
pydicom is a pure python package for working with DICOM files. It was made
for inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file. As a pure python package,
it should run anywhere python runs without any other requirements.

%prep
%setup -q -n py%{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
#sed -i 's/.*egg-info$//' FILELIST

%clean

%files -f FILELIST


