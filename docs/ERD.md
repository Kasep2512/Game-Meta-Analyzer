erDiagram
    HEROES {
        int id PK
        string name
        string role
    }

    PATCH_NOTES {
        int id PK
        string version_number
        date release_date
        text description
    }

    HERO_STATS {
        int id PK
        int hero_id FK
        int patch_id FK
        float win_rate
        float pick_rate
        float ban_rate
    }

    TOURNAMENT {
        int id PK
        string name
        date start_date
        date end_date
    }

    MATCHES {
        int id PK
        int tournament_id FK
        string team_blue
        string team_red
        string winner
        date match_date
    }

    HEROES ||--o{ HERO_STATS : "memiliki" }
    PATCH_NOTES ||--o{ HERO_STATS : "dianalisis pada" }
    TOURNAMENT ||--o{ MATCHES : "menyelenggarakan" }