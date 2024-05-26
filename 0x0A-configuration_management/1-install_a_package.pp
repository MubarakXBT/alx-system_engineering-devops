# Install flask

package { 'werkzeug':
  ensure   => '2.3.0',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
