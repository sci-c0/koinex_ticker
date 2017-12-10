
1. Need some library to fetch/download [Cryptocurrency rates URL](https://koinex.in/api/ticker) provided by [Koinex](https://koinex.in): Download **`pycurl`** source
2. Compile and install **pycurl**
	* **`python setup.py install`**
	* Needs curl-config; Provided By:
		* **[libcurl4-openssl-dev](https://packages.debian.org/jessie/libcurl4-openssl-dev)** OR 
		* **[libcurl4-gnutls-dev](https://packages.debian.org/jessie/libcurl4-gnutls-dev)** OR 
		* **[libcurl4-nss-dev](https://packages.debian.org/jessie/libcurl4-nss-dev)**
	* Used: **`apt-get install libcurl4-openssl-dev`**
	* Needs SSL headers: Provided By **libssl-dev**: **`apt-get install libssl-dev`**

