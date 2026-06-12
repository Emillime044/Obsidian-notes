## Funzionamento CSRF (Cross Site Request Forgery)

### Condizioni

1. Funzionalità sul sito target che l'attaccante vuole manipolare;
2. Gestione della sessione basata sui cookie;
3. Parametri prevedibili;

##  Passaggi

1. Autenticazione della vittima: 
	1. Utente accede legittimamente al sito web vulnerabile inserendo le proprie credenziali;
	2. Server convalida accesso e rilascia un cookie di sessione che viene salvato nel browser dell'utente;
	3. Utente lascia la scheda aperta o non effettua il logout;
2. Inganno (Social Engineering):
	1. Attaccante attira utente su un sito web maligno controllato da lui o fa visualizzare un email in formato HTML contenente codice malevolo
3. Iniezione della richiesta forzata:
	1. All'interno del codice HTML/JavaScript del sito trappola, attaccante ha predisposto una richiesta nascosta indirizzata al sito vulnerabile.
4. Invio automatico dei cookie:
	1. Browser dell'utente esegue una richiesta verso il sito legittimo;
	2. Il cookie di sessione valido della vittima viene allegato alla richiesta malevola;
5. Esecuzione sul Server:
	1. Il server richiede la richiesta, controlla il cookie, vede che appartiene a un utente autenticato