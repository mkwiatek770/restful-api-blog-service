# Enpoints
1. Blogs
* /blogs/ GET    Lista wsyztkich artykułów  Dostępne dla wszystkui
* /blogs/ POST   Tworzenie artykułu 
* /blogs/<int:id>/ GET  Otwieranie jakiegoś artykułu
* /blogs/<int:id>/ PUT Modyfikacja całego artykułu, wszystkich pól
* /blogs/<int:id>/ PATCH Modyfikacja pojedyńczych pól artykułu
* /blogs/<int:id>/ DELETE Usuwanie artykułu
2. Users & Authentication
* /login/ POST Logowanie się jako zalogowany użytkownik
* /register/ POST założenie nowego konta
