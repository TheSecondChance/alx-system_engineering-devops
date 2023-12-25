

file { 'etc/ssh/shh_config':
	ensure => present,

content =>"
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
