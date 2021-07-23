@startuml
    skinparam Style strictuml

    title Diagramme de séquence

    == Récupération du WS et envoi en base ==
        API_Back -> Web_Service : Requete
        Web_Service -> API_Back : Reponse JSON
        API_Back -> BDD : envoi

    == Affichage de la requete ==
        Client -> API_Back : Requete
        API_Back -> BDD : Requete SQL
        BDD -> API_Back : Réponse
        API_Back -> Client : Affichage

@enduml