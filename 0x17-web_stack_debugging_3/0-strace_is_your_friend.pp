# Fixes an Apache 500 error

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Exec['fix-wordpress'],  # Ensure the file is modified after the fix is applied
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
