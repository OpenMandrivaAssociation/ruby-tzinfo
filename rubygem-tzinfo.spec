%define oname tzinfo

Name:       ruby-%{oname}
Version:    0.3.33
Release:    1
Summary:    Daylight-savings aware timezone library
Group:      Development/Ruby
License:    MIT
URL:        http://tzinfo.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRequires: rubygems
BuildArch:  noarch
%rename     rubygem-%{oname}

%description
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.


%prep

%build

%install
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
