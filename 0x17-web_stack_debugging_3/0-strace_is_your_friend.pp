# Fixes Apache 500 error.

file { '/etc/apache2/sites-available/000-default.conf':
	ensure  => present,
	content => '
		<VirtualHost *:80>
			ServerAdmin webmaster@localhost
			DocumentRoot /var/www/html
			ErrorLog ${APACHE_LOG_DIR}/error.log
			CustomLog ${APACHE_LOG_DIR}/access.log combined
		</VirtualHost>
',
	owner   => 'root',
	group   => 'root',
	mode    => '0644',
}

service { 'apache2':
	ensure  => running,
	require => File['/etc/apache2/sites-available/000-default.conf'],
}
