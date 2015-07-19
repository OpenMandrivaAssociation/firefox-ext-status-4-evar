Summary:	Firefox extension for customizing the status panel
Name:		firefox-ext-status-4-evar
Version:	2015.02.06.23
Release:	2
License:	GPLv2+
Group:		Networking/WWW
Url:		https://addons.mozilla.org/en-US/firefox/addon/status-4-evar
Source0:	https://addons.mozilla.org/firefox/downloads/latest/235283/addon-235283-latest.xpi
Buildarch:	noarch

BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_version}

%description
Firefox extension for customizing the status panel

%prep
%setup -qc

%install
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
	hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
	echo "Failed to find plugin hash."
	exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%files
%{firefox_extdir}/*
