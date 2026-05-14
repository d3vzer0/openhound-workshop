[![PokéAPI](https://pokeapi.co/static/pokeapi_256.3fa72200.png)](https://pokeapi.co/ "PokéAPI") [Home](https://pokeapi.co/) [About](https://pokeapi.co/about) [API v2](https://pokeapi.co/docs/v2) [GraphQL](https://pokeapi.co/docs/graphql)

Starting June 18th a new GraphQL specification is rolling out, v1beta2. Read more at [GraphQL v1beta2](https://pokeapi.co/docs/graphql#v1beta2). The former v1beta version is sun-setting and scheduled to be removed.

Dismiss

## Contents

- [Information](https://pokeapi.co/docs/v2#info)
- [Fair Use Policy](https://pokeapi.co/docs/v2#fairuse)
- [Slack](https://pokeapi.co/docs/v2#slack)
- [Wrapper Libraries](https://pokeapi.co/docs/v2#wrap)
- [Resource Lists/Pagination](https://pokeapi.co/docs/v2#resource-listspagination-section)
  - [Named](https://pokeapi.co/docs/v2#named)
  - [Unnamed](https://pokeapi.co/docs/v2#unnamed)
- [Berries](https://pokeapi.co/docs/v2#berries-section)
  - [Berries](https://pokeapi.co/docs/v2#berries)
  - [Berry Firmnesses](https://pokeapi.co/docs/v2#berry-firmnesses)
  - [Berry Flavors](https://pokeapi.co/docs/v2#berry-flavors)
- [Contests](https://pokeapi.co/docs/v2#contests-section)
  - [Contest Types](https://pokeapi.co/docs/v2#contest-types)
  - [Contest Effects](https://pokeapi.co/docs/v2#contest-effects)
  - [Super Contest Effects](https://pokeapi.co/docs/v2#super-contest-effects)
- [Encounters](https://pokeapi.co/docs/v2#encounters-section)
  - [Encounter Methods](https://pokeapi.co/docs/v2#encounter-methods)
  - [Encounter Conditions](https://pokeapi.co/docs/v2#encounter-conditions)
  - [Encounter Condition Values](https://pokeapi.co/docs/v2#encounter-condition-values)
- [Evolution](https://pokeapi.co/docs/v2#evolution-section)
  - [Evolution Chains](https://pokeapi.co/docs/v2#evolution-chains)
  - [Evolution Triggers](https://pokeapi.co/docs/v2#evolution-triggers)
- [Games](https://pokeapi.co/docs/v2#games-section)
  - [Generations](https://pokeapi.co/docs/v2#generations)
  - [Pokedexes](https://pokeapi.co/docs/v2#pokedexes)
  - [Version](https://pokeapi.co/docs/v2#version)
  - [Version Groups](https://pokeapi.co/docs/v2#version-groups)
- [Items](https://pokeapi.co/docs/v2#items-section)
  - [Item](https://pokeapi.co/docs/v2#item)
  - [Item Attributes](https://pokeapi.co/docs/v2#item-attributes)
  - [Item Categories](https://pokeapi.co/docs/v2#item-categories)
  - [Item Fling Effects](https://pokeapi.co/docs/v2#item-fling-effects)
  - [Item Pockets](https://pokeapi.co/docs/v2#item-pockets)
- [Locations](https://pokeapi.co/docs/v2#locations-section)
  - [Locations](https://pokeapi.co/docs/v2#locations)
  - [Location Areas](https://pokeapi.co/docs/v2#location-areas)
  - [Pal Park Areas](https://pokeapi.co/docs/v2#pal-park-areas)
  - [Regions](https://pokeapi.co/docs/v2#regions)
- [Machines](https://pokeapi.co/docs/v2#machines-section)
  - [Machines](https://pokeapi.co/docs/v2#machines)
- [Moves](https://pokeapi.co/docs/v2#moves-section)
  - [Moves](https://pokeapi.co/docs/v2#moves)
  - [Move Ailments](https://pokeapi.co/docs/v2#move-ailments)
  - [Move Battle Styles](https://pokeapi.co/docs/v2#move-battle-styles)
  - [Move Categories](https://pokeapi.co/docs/v2#move-categories)
  - [Move Damage Classes](https://pokeapi.co/docs/v2#move-damage-classes)
  - [Move Learn Methods](https://pokeapi.co/docs/v2#move-learn-methods)
  - [Move Targets](https://pokeapi.co/docs/v2#move-targets)
- [Pokémon](https://pokeapi.co/docs/v2#pokemon-section)
  - [Abilities](https://pokeapi.co/docs/v2#abilities)
  - [Characteristics](https://pokeapi.co/docs/v2#characteristics)
  - [Egg Groups](https://pokeapi.co/docs/v2#egg-groups)
  - [Genders](https://pokeapi.co/docs/v2#genders)
  - [Growth Rates](https://pokeapi.co/docs/v2#growth-rates)
  - [Natures](https://pokeapi.co/docs/v2#natures)
  - [Pokeathlon Stats](https://pokeapi.co/docs/v2#pokeathlon-stats)
  - [Pokemon](https://pokeapi.co/docs/v2#pokemon)
  - [Pokemon Location Areas](https://pokeapi.co/docs/v2#pokemon-location-areas)
  - [Pokemon Colors](https://pokeapi.co/docs/v2#pokemon-colors)
  - [Pokemon Forms](https://pokeapi.co/docs/v2#pokemon-forms)
  - [Pokemon Habitats](https://pokeapi.co/docs/v2#pokemon-habitats)
  - [Pokemon Shapes](https://pokeapi.co/docs/v2#pokemon-shapes)
  - [Pokemon Species](https://pokeapi.co/docs/v2#pokemon-species)
  - [Stats](https://pokeapi.co/docs/v2#stats)
  - [Types](https://pokeapi.co/docs/v2#types)
- [Utility](https://pokeapi.co/docs/v2#utility-section)
  - [Languages](https://pokeapi.co/docs/v2#languages)
  - [Common Models](https://pokeapi.co/docs/v2#common-models)

If you were using v1 of this API, please switch to v2 (this page). [Read more…](https://pokeapi.co/docs/v1)

**Quick tip:** Use your browser's "find on page" feature to search for specific resource types ( `Ctrl+F` or `Cmd+F`).

## Information

This is a **consumption-only** API — only the HTTP GET method is available on resources.

No authentication is required to access this API, and all resources are fully open and available. Since the move to static hosting in November 2018, rate limiting has been removed entirely, but we still encourage you to limit the frequency of requests to limit our hosting costs.

## Fair Use Policy

PokéAPI is free and open to use. It is also very popular. Because of this, we ask every developer to abide by our fair use policy. People not complying with the fair use policy will have their IP address permanently banned.

PokéAPI is primarily an educational tool, and we will not tolerate denial of service attacks preventing people from learning.

Rules:

- Locally cache resources whenever you request them.
- Be nice and friendly to your fellow PokéAPI developers.
- If you spot security vulnerabilities act and [report them](https://github.com/PokeAPI/pokeapi/blob/master/SECURITY.md#reporting-a-vulnerability) responsibly.

## Slack and community

Currently no maintainer has enough free time to support the community on Slack. Our Slack is in an unmaintained status. You can still sign up right [here](https://join.slack.com/t/pokeapi/shared_invite/zt-2ampo6her-_tHSI3uOS65WzGypt7Y96w) then visit our [Slack](https://pokeapi.slack.com/) page.

## Wrapper Libraries

- **Node Server-side with auto caching**: [Pokedex Promise v2](https://github.com/PokeAPI/pokedex-promise-v2) by Thomas Asadurian and Alessandro Pezzé
- **Browser-side with auto caching**: [pokeapi-js-wrapper](https://github.com/PokeAPI/pokeapi-js-wrapper) by Alessandro Pezzé
- **Python 3 with auto caching**: [PokeBase](https://github.com/GregHilmes/pokebase) by Greg Hilmes
- **Python 2/3 with auto caching**: [Pokepy](https://github.com/PokeAPI/pokepy) by Paul Hallett
- **Kotlin Multiplatform (JVM, Native, Browser, and Node) with auto caching**: [PokeKotlin](https://github.com/PokeAPI/pokekotlin) by sargunv
- **Java (Spring Boot) with auto caching**: [pokeapi-reactor](https://github.com/SirSkaro/pokeapi-reactor) by Benjamin Churchill
- **.NET (C#, VB, etc)**: [PokeApi.NET](https://gitlab.com/PoroCYon/PokeApi.NET) by PoroCYon
- **.NET Standard**: [PokeApiNet](https://github.com/mtrdp642/PokeApiNet) by mtrdp642
- **Swift**: [PokemonAPI](https://github.com/kinkofer/PokemonAPI) by kinkofer
- **PHP**: [PokePHP](https://github.com/danrovito/pokephp) by Dan Rovito
- **PHP**: [PHPokéAPI](https://github.com/lmerotta/phpokeapi) by lmerotta
- **Ruby**: [Poke-Api-V2](https://github.com/rdavid1099/poke-api-v2) by rdavid1099
- **Go**: [pokeapi-go](https://github.com/mtslzr/pokeapi-go) by mtslzr
- **Go**: [PokeGo](https://github.com/JoshGuarino/PokeGo) by Josh Guarino
- **Crystal**: [pokeapi](https://github.com/henrikac/pokeapi) by henrikac
- **Typescript with auto caching**: [Pokenode-ts](https://github.com/Gabb-c/pokenode-ts) by Gabb-c
- **Rust with auto caching**: [Rustemon](https://crates.io/crates/rustemon) by mlemesle
- **Asynchronous Python wrapper with auto caching**: [aiopokeapi](https://github.com/beastmatser/aiopokeapi) by beastmatser
- **Scala 3 with auto caching**: [pokeapi-scala](https://github.com/juliano/pokeapi-scala) by Juliano Alves
- **Elixir wrapper with auto caching**: [Max-Elixir-PokeAPI](https://github.com/HenriqueArtur/Max-Elixir-PokeAPI) by Henrique Artur

## Resource Lists/Pagination (group)

Calling any API endpoint without a resource ID or name will return a paginated list of available resources for that API. By default, a list "page" will contain up to 20 resources. If you would like to change this just add a 'limit' query parameter to the GET request, e.g. `?limit=60`. You can use 'offset' to move to the next page, e.g. `?limit=60&offset=60`. `characteristic`, `contest-effect`, `evolution-chain`, `machine`, `super-contest-effect` endpoints are unnamed, the rest are named.

### Named (endpoint)

GET https://pokeapi.co/api/v2/{endpoint}/

- count:248
- next:"https://pokeapi.co/api/v2/ability/?limit=20&offset=20"
- previous:null
- ▶


results:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"stench"
    - url:"https://pokeapi.co/api/v2/ability/1/"

View raw JSON (0.213 kB, 11 lines)

#### NamedAPIResourceList (type)

| Name | Description | Type |
| --- | --- | --- |
| count | The total number of resources available from this API. | _integer_ |
| next | The URL for the next page in the list. | _string_ |
| previous | The URL for the previous page in the list. | _string_ |
| results | A list of named API resources. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ |

### Unnamed (endpoint)

GET https://pokeapi.co/api/v2/{endpoint}/

- count:541
- next:"https://pokeapi.co/api/v2/evolution-chain?offset=20&limit=20"
- previous:null
- ▶


results:\[\] 1 item
  - ▶


    0:{} 1 key
    - url:"https://pokeapi.co/api/v2/evolution-chain/1/"

View raw JSON (0.204 kB, 10 lines)

#### APIResourceList (type)

| Name | Description | Type |
| --- | --- | --- |
| count | The total number of resources available from this API. | _integer_ |
| next | The URL for the next page in the list. | _string_ |
| previous | The URL for the previous page in the list. | _string_ |
| results | A list of unnamed API resources. | list _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ |

## Berries (group)

### Berries (endpoint)

Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Berry) for greater detail.

GET https://pokeapi.co/api/v2/berry/{id or name}/

- id:1
- name:"cheri"
- growth\_time:3
- max\_harvest:5
- natural\_gift\_power:60
- size:20
- smoothness:25
- soil\_dryness:15
- ▶


firmness:{} 2 keys
  - name:"soft"
  - url:"https://pokeapi.co/api/v2/berry-firmness/2/"
- ▶


flavors:\[\] 1 item
  - ▶


    0:{} 2 keys
    - potency:10
    - ▶


      flavor:{} 2 keys
      - name:"spicy"
      - url:"https://pokeapi.co/api/v2/berry-flavor/1/"
- ▶


item:{} 2 keys
  - name:"cheri-berry"
  - url:"https://pokeapi.co/api/v2/item/126/"
- ▶


natural\_gift\_type:{} 2 keys
  - name:"fire"
  - url:"https://pokeapi.co/api/v2/type/10/"

View raw JSON (0.608 kB, 31 lines)

#### Berry (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| growth\_time | Time it takes the tree to grow one stage, in hours. Berry trees go through four of these growth stages before they can be picked. | _integer_ |
| max\_harvest | The maximum number of these berries that can grow on one tree in Generation IV. | _integer_ |
| natural\_gift\_power | The power of the move "Natural Gift" when used with this Berry. | _integer_ |
| size | The size of this Berry, in millimeters. | _integer_ |
| smoothness | The smoothness of this Berry, used in making Pokéblocks or Poffins. | _integer_ |
| soil\_dryness | The speed at which this Berry dries out the soil as it grows. A higher rate means the soil dries more quickly. | _integer_ |
| firmness | The firmness of this berry, used in making Pokéblocks or Poffins. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[BerryFirmness](https://pokeapi.co/docs/v2#berryfirmness)_) |
| flavors | A list of references to each flavor a berry can have and the potency of each of those flavors in regard to this berry. | list _[BerryFlavorMap](https://pokeapi.co/docs/v2#berryflavormap)_ |
| item | Berries are actually items. This is a reference to the item specific data for this berry. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| natural\_gift\_type | The type inherited by "Natural Gift" when used with this Berry. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |

#### BerryFlavorMap (type)

| Name | Description | Type |
| --- | --- | --- |
| potency | How powerful the referenced flavor is for this berry. | _integer_ |
| flavor | The referenced berry flavor. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[BerryFlavor](https://pokeapi.co/docs/v2#berryflavor)_) |

### Berry Firmnesses (endpoint)

Berries can be soft or hard. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Category:Berries_by_firmness) for greater detail.

GET https://pokeapi.co/api/v2/berry-firmness/{id or name}/

- id:1
- name:"very-soft"
- ▶


berries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"pecha"
    - url:"https://pokeapi.co/api/v2/berry/3/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Very Soft"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.303 kB, 19 lines)

#### BerryFirmness (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| berries | A list of the berries with this firmness. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Berry](https://pokeapi.co/docs/v2#berry))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Berry Flavors (endpoint)

Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their [nature](https://pokeapi.co/docs/v2#natures). Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Flavor) for greater detail.

GET https://pokeapi.co/api/v2/berry-flavor/{id or name}/

- id:1
- name:"spicy"
- ▶


berries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - potency:10
    - ▶


      berry:{} 2 keys
      - name:"rowap"
      - url:"https://pokeapi.co/api/v2/berry/64/"
- ▶


contest\_type:{} 2 keys
  - name:"cool"
  - url:"https://pokeapi.co/api/v2/contest-type/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Spicy"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.446 kB, 26 lines)

#### BerryFlavor (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| berries | A list of the berries with this flavor. | list _[FlavorBerryMap](https://pokeapi.co/docs/v2#flavorberrymap)_ |
| contest\_type | The contest type that correlates with this berry flavor. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[ContestType](https://pokeapi.co/docs/v2#contesttype)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

#### FlavorBerryMap (type)

| Name | Description | Type |
| --- | --- | --- |
| potency | How powerful the referenced flavor is for this berry. | _integer_ |
| berry | The berry with the referenced flavor. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Berry](https://pokeapi.co/docs/v2#berry)_) |

## Contests (group)

### Contest Types (endpoint)

Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Contest_condition) for greater detail.

GET https://pokeapi.co/api/v2/contest-type/{id or name}/

- id:1
- name:"cool"
- ▶


berry\_flavor:{} 2 keys
  - name:"spicy"
  - url:"https://pokeapi.co/api/v2/berry-flavor/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 3 keys
    - name:"Cool"
    - color:"Red"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.311 kB, 18 lines)

#### ContestType (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| berry\_flavor | The berry flavor that correlates with this contest type. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[BerryFlavor](https://pokeapi.co/docs/v2#berryflavor)_) |
| names | The name of this contest type listed in different languages. | list _[ContestName](https://pokeapi.co/docs/v2#contestname)_ |

#### ContestName (type)

| Name | Description | Type |
| --- | --- | --- |
| name | The name for this contest. | _string_ |
| color | The color associated with this contest's name. | _string_ |
| language | The language that this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

### Contest Effects (endpoint)

Contest effects refer to the effects of moves when used in contests.

GET https://pokeapi.co/api/v2/contest-effect/{id}/

- id:1
- appeal:4
- jam:0
- ▶


effect\_entries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - effect:"Gives a high number of appeal points wth no other effects."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - flavor\_text:"A highly appealing move."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.46 kB, 23 lines)

#### ContestEffect (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| appeal | The base number of hearts the user of this move gets. | _integer_ |
| jam | The base number of hearts the user's opponent loses. | _integer_ |
| effect\_entries | The result of this contest effect listed in different languages. | list _[Effect](https://pokeapi.co/docs/v2#effect)_ |
| flavor\_text\_entries | The flavor text of this contest effect listed in different languages. | list _[ContestEffectFlavorText](https://pokeapi.co/docs/v2#contesteffectflavortext)_ |

#### ContestEffectFlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| flavor\_text | The localized flavor text for an API resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

### Super Contest Effects (endpoint)

Super contest effects refer to the effects of moves when used in super contests.

GET https://pokeapi.co/api/v2/super-contest-effect/{id}/

- id:1
- appeal:2
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - flavor\_text:"Enables the user to perform first in the next turn."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"agility"
    - url:"https://pokeapi.co/api/v2/move/97/"

View raw JSON (0.358 kB, 19 lines)

#### SuperContestEffect (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| appeal | The level of appeal this super contest effect has. | _integer_ |
| flavor\_text\_entries | The flavor text of this super contest effect listed in different languages. | list _[SuperContestEffectFlavorText](https://pokeapi.co/docs/v2#supercontesteffectflavortext)_ |
| moves | A list of moves that have the effect when used in super contests. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |

#### SuperContestEffectFlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| flavor\_text | The localized flavor text for an API resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

## Encounters (group)

### Encounter Methods (endpoint)

Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall grass. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Wild_Pok%C3%A9mon) for greater detail.

GET https://pokeapi.co/api/v2/encounter-method/{id or name}/

- id:1
- name:"walk"
- order:1
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Walking in tall grass or a cave"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.229 kB, 14 lines)

#### EncounterMethod (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| order | A good value for sorting. | _integer_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Encounter Conditions (endpoint)

Conditions which affect what pokemon might appear in the wild, e.g., day or night.

GET https://pokeapi.co/api/v2/encounter-condition/{id or name}/

- id:1
- name:"swarm"
- ▶


values:\[\] 2 items
  - ▶


    0:{} 2 keys
    - name:"swarm-yes"
    - url:"https://pokeapi.co/api/v2/encounter-condition-value/1/"
  - ▶


    1:{} 2 keys
    - name:"swarm-no"
    - url:"https://pokeapi.co/api/v2/encounter-condition-value/2/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Schwarm"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"

View raw JSON (0.429 kB, 23 lines)

#### EncounterCondition (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| values | A list of possible values for this encounter condition. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([EncounterConditionValue](https://pokeapi.co/docs/v2#encounterconditionvalue))_ |

### Encounter Condition Values (endpoint)

Encounter condition values are the various states that an encounter condition can have, i.e., time of day can be either day or night.

GET https://pokeapi.co/api/v2/encounter-condition-value/{id or name}/

- id:1
- name:"swarm-yes"
- ▶


condition:{} 2 keys
  - name:"swarm"
  - url:"https://pokeapi.co/api/v2/encounter-condition/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"WÃ¤hrend eines Schwarms"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"

View raw JSON (0.319 kB, 17 lines)

#### EncounterConditionValue (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| condition | The condition this encounter condition value pertains to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[EncounterCondition](https://pokeapi.co/docs/v2#encountercondition)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

## Evolution (group)

### Evolution Chains (endpoint)

Evolution chains are essentially family trees. They start with the lowest stage within a family and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.

GET https://pokeapi.co/api/v2/evolution-chain/{id}/

- id:7
- baby\_trigger\_item:null
- ▶


chain:{} 4 keys

View raw JSON (1.227 kB, 47 lines)

#### EvolutionChain (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| baby\_trigger\_item | The item that a Pokémon would be holding when mating that would trigger the egg hatching a baby Pokémon rather than a basic Pokémon. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| chain | The base chain link object. Each link contains evolution details for a Pokémon in the chain. Each link references the next Pokémon in the natural evolution order. | [ChainLink](https://pokeapi.co/docs/v2#chainlink) |

#### ChainLink (type)

| Name | Description | Type |
| --- | --- | --- |
| is\_baby | Whether or not this link is for a baby Pokémon. This would only ever be true on the base link. | _boolean_ |
| species | The Pokémon species at this point in the evolution chain. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |
| evolution\_details | All details regarding the specific details of the referenced Pokémon species evolution. | list _[EvolutionDetail](https://pokeapi.co/docs/v2#evolutiondetail)_ |
| evolves\_to | A List of chain objects. | list _[ChainLink](https://pokeapi.co/docs/v2#chainlink)_ |

#### EvolutionDetail (type)

| Name | Description | Type |
| --- | --- | --- |
| item | The item required to cause evolution this into Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| trigger | The type of event that triggers evolution into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[EvolutionTrigger](https://pokeapi.co/docs/v2#evolutiontrigger)_) |
| gender | The id of the gender of the evolving Pokémon species must be in order to evolve into this Pokémon species. | _integer_ |
| held\_item | The item the evolving Pokémon species must be holding during the evolution trigger event to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| known\_move | The move that must be known by the evolving Pokémon species during the evolution trigger event in order to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Move](https://pokeapi.co/docs/v2#move)_) |
| known\_move\_type | The evolving Pokémon species must know a move with this type during the evolution trigger event in order to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |
| location | The location the evolution must be triggered at. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Location](https://pokeapi.co/docs/v2#location)_) |
| min\_level | The minimum required level of the evolving Pokémon species to evolve into this Pokémon species. | _integer_ |
| min\_happiness | The minimum required level of happiness the evolving Pokémon species to evolve into this Pokémon species. | _integer_ |
| min\_beauty | The minimum required level of beauty the evolving Pokémon species to evolve into this Pokémon species. | _integer_ |
| min\_affection | The minimum required level of affection the evolving Pokémon species to evolve into this Pokémon species. | _integer_ |
| needs\_multiplayer | Whether or not multiplayer link play is needed to evolve into this Pokémon species (e.g. Union Circle). | _boolean_ |
| needs\_overworld\_rain | Whether or not it must be raining in the overworld to cause evolution this Pokémon species. | _boolean_ |
| party\_species | The Pokémon species that must be in the players party in order for the evolving Pokémon species to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |
| party\_type | The player must have a Pokémon of this type in their party during the evolution trigger event in order for the evolving Pokémon species to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |
| relative\_physical\_stats | The required relation between the Pokémon's Attack and Defense stats. 1 means Attack > Defense. 0 means Attack = Defense. -1 means Attack < Defense. | _integer_ |
| time\_of\_day | The required time of day. Day or night. | _string_ |
| trade\_species | Pokémon species for which this one must be traded. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |
| turn\_upside\_down | Whether or not the 3DS needs to be turned upside-down as this Pokémon levels up. | _boolean_ |
| region | The required region in which this evolution can occur. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Region](https://pokeapi.co/docs/v2#region)_) |
| base\_form | The required form for which this evolution can occur. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |
| used\_move | The move that must be used by the evolving Pokémon species during the evolution trigger event in order to evolve into this Pokémon species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Move](https://pokeapi.co/docs/v2#move)_) |
| min\_move\_count | The minimum number of times a move must be used in order to evolve into this Pokémon species. | _integer_ |
| min\_steps | The minimum number of steps that must be taken in order to evolve into this Pokémon species. | _integer_ |
| min\_damage\_taken | The minimum amount of damage taken during the evolution trigger event in order to evolve into this Pokémon species. | _integer_ |

### Evolution Triggers (endpoint)

Evolution triggers are the events and conditions that cause a Pokémon to evolve. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Methods_of_evolution) for greater detail.

GET https://pokeapi.co/api/v2/evolution-trigger/{id or name}/

- id:1
- name:"level-up"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Level up"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"ivysaur"
    - url:"https://pokeapi.co/api/v2/pokemon-species/2/"

View raw JSON (0.321 kB, 19 lines)

#### EvolutionTrigger (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_species | A list of pokemon species that result from this evolution trigger. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

## Games (group)

### Generations (endpoint)

A generation is a grouping of the Pokémon games that separates them based on the Pokémon they include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not exist in the previous generation are released.

GET https://pokeapi.co/api/v2/generation/{id or name}/

- id:1
- name:"generation-i"
- abilities:\[\] 0 items
- ▶


main\_region:{} 2 keys
  - name:"kanto"
  - url:"https://pokeapi.co/api/v2/region/1/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"pound"
    - url:"https://pokeapi.co/api/v2/move/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Generation I"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"bulbasaur"
    - url:"https://pokeapi.co/api/v2/pokemon-species/1/"
- ▶


types:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"normal"
    - url:"https://pokeapi.co/api/v2/type/1/"
- ▶


version\_groups:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"red-blue"
    - url:"https://pokeapi.co/api/v2/version-group/1/"

View raw JSON (0.772 kB, 42 lines)

#### Generation (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| abilities | A list of abilities that were introduced in this generation. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Ability](https://pokeapi.co/docs/v2#ability))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| main\_region | The main region travelled in this generation. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Region](https://pokeapi.co/docs/v2#region)_) |
| moves | A list of moves that were introduced in this generation. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| pokemon\_species | A list of Pokémon species that were introduced in this generation. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |
| types | A list of types that were introduced in this generation. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| version\_groups | A list of version groups that were introduced in this generation. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([VersionGroup](https://pokeapi.co/docs/v2#versiongroup))_ |

### Pokedexes (endpoint)

A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokémon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pokedex) for greater detail.

GET https://pokeapi.co/api/v2/pokedex/{id or name}/

- id:2
- name:"kanto"
- is\_main\_series:true
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Rot/Blau/Gelb Kanto Dex"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Kanto"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


pokemon\_entries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - entry\_number:1
    - ▶


      pokemon\_species:{} 2 keys
      - name:"bulbasaur"
      - url:"https://pokeapi.co/api/v2/pokemon-species/1/"
- ▶


region:{} 2 keys
  - name:"kanto"
  - url:"https://pokeapi.co/api/v2/region/1/"
- ▶


version\_groups:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"red-blue"
    - url:"https://pokeapi.co/api/v2/version-group/1/"

View raw JSON (0.809 kB, 42 lines)

#### Pokedex (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| is\_main\_series | Whether or not this Pokédex originated in the main series of the video games. | _boolean_ |
| descriptions | The description of this resource listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_entries | A list of Pokémon catalogued in this Pokédex and their indexes. | list _[PokemonEntry](https://pokeapi.co/docs/v2#pokemonentry)_ |
| region | The region this Pokédex catalogues Pokémon for. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Region](https://pokeapi.co/docs/v2#region)_) |
| version\_groups | A list of version groups this Pokédex is relevant to. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([VersionGroup](https://pokeapi.co/docs/v2#versiongroup))_ |

#### PokemonEntry (type)

| Name | Description | Type |
| --- | --- | --- |
| entry\_number | The index of this Pokémon species entry within the Pokédex. | _integer_ |
| pokemon\_species | The Pokémon species being encountered. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |

### Version (endpoint)

Versions of the games, e.g., Red, Blue or Yellow.

GET https://pokeapi.co/api/v2/version/{id or name}/

- id:1
- name:"red"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Rot"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


version\_group:{} 2 keys
  - name:"red-blue"
  - url:"https://pokeapi.co/api/v2/version-group/1/"

View raw JSON (0.292 kB, 17 lines)

#### Version (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| version\_group | The version group this version belongs to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

### Version Groups (endpoint)

Version groups categorize highly similar versions of the games.

GET https://pokeapi.co/api/v2/version-group/{id or name}/

- id:1
- name:"red-blue"
- order:1
- ▶


generation:{} 2 keys
  - name:"generation-i"
  - url:"https://pokeapi.co/api/v2/generation/1/"
- ▶


move\_learn\_methods:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"level-up"
    - url:"https://pokeapi.co/api/v2/move-learn-method/1/"
- ▶


pokedexes:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"kanto"
    - url:"https://pokeapi.co/api/v2/pokedex/2/"
- ▶


regions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"kanto"
    - url:"https://pokeapi.co/api/v2/region/1/"
- ▶


versions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"red"
    - url:"https://pokeapi.co/api/v2/version/1/"

View raw JSON (0.605 kB, 33 lines)

#### VersionGroup (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| order | Order for sorting. Almost by date of release, except similar versions are grouped together. | _integer_ |
| generation | The generation this version was introduced in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| move\_learn\_methods | A list of methods in which Pokémon can learn moves in this version group. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([MoveLearnMethod](https://pokeapi.co/docs/v2#movelearnmethod))_ |
| pokedexes | A list of Pokédexes introduces in this version group. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Pokedex](https://pokeapi.co/docs/v2#pokedex))_ |
| regions | A list of regions that can be visited in this version group. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Region](https://pokeapi.co/docs/v2#region))_ |
| versions | The versions this version group owns. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Version](https://pokeapi.co/docs/v2#version))_ |

## Items (group)

### Item (endpoint)

An item is an object in the games which the player can pick up, keep in their bag, and use in some manner. They have various uses, including healing, powering up, helping catch Pokémon, or to access a new area.

GET https://pokeapi.co/api/v2/item/{id or name}/

- id:1
- name:"master-ball"
- cost:0
- fling\_power:10
- ▶


fling\_effect:{} 2 keys
  - name:"flinch"
  - url:"https://pokeapi.co/api/v2/item-fling-effect/7/"
- ▶


attributes:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"holdable"
    - url:"https://pokeapi.co/api/v2/item-attribute/5/"
- ▶


category:{} 2 keys
  - name:"standard-balls"
  - url:"https://pokeapi.co/api/v2/item-category/34/"
- ▶


effect\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - effect:"Used in battle
      : \[Catches\]{mechanic:catch} a wild Pokémon without fail.

       If used in a trainer battle, nothing happens and the ball is lost."
    - short\_effect:"Catches a wild Pokémon every time."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - text:"The best Poké Ball with the ultimate level of performance. With it, you will catch any wild Pokémon without fail."
    - ▶


      version\_group:{} 2 keys
      - name:"x-y"
      - url:"https://pokeapi.co/api/v2/version-group/15/"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


game\_indices:\[\] 1 item
  - ▶


    0:{} 2 keys
    - game\_index:1
    - ▶


      generation:{} 2 keys
      - name:"generation-vi"
      - url:"https://pokeapi.co/api/v2/generation/6/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Master Ball"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


sprites:{} 1 key
  - default:"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png"
- ▶


held\_by\_pokemon:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      pokemon:{} 2 keys
      - name:"chansey"
      - url:"https://pokeapi.co/api/v2/pokemon/113/"
    - ▶


      version\_details:\[\] 1 item
- ▶


baby\_trigger\_for:{} 1 key
  - url:"https://pokeapi.co/api/v2/evolution-chain/1/"

View raw JSON (2.094 kB, 84 lines)

#### Item (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| cost | The price of this item in stores. | _integer_ |
| fling\_power | The power of the move Fling when used with this item. | _integer_ |
| fling\_effect | The effect of the move Fling when used with this item. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[ItemFlingEffect](https://pokeapi.co/docs/v2#itemflingeffect)_) |
| attributes | A list of attributes this item has. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([ItemAttribute](https://pokeapi.co/docs/v2#itemattribute))_ |
| category | The category of items this item falls into. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[ItemCategory](https://pokeapi.co/docs/v2#itemcategory)_) |
| effect\_entries | The effect of this ability listed in different languages. | list _[VerboseEffect](https://pokeapi.co/docs/v2#verboseeffect)_ |
| flavor\_text\_entries | The flavor text of this ability listed in different languages. | list _[VersionGroupFlavorText](https://pokeapi.co/docs/v2#versiongroupflavortext)_ |
| game\_indices | A list of game indices relevent to this item by generation. | list _[GenerationGameIndex](https://pokeapi.co/docs/v2#generationgameindex)_ |
| names | The name of this item listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| sprites | A set of sprites used to depict this item in the game. | [ItemSprites](https://pokeapi.co/docs/v2#itemsprites) |
| held\_by\_pokemon | A list of Pokémon that might be found in the wild holding this item. | list _[ItemHolderPokemon](https://pokeapi.co/docs/v2#itemholderpokemon)_ |
| baby\_trigger\_for | An evolution chain this item requires to produce a bay during mating. | _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ ( _[EvolutionChain](https://pokeapi.co/docs/v2#evolutionchain)_) |
| machines | A list of the machines related to this item. | list _[MachineVersionDetail](https://pokeapi.co/docs/v2#machineversiondetail)_ |

#### ItemSprites (type)

| Name | Description | Type |
| --- | --- | --- |
| default | The default depiction of this item. | _string_ |

#### ItemHolderPokemon (type)

| Name | Description | Type |
| --- | --- | --- |
| pokemon | The Pokémon that holds this item. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |
| version\_details | The details for the version that this item is held in by the Pokémon. | list _[ItemHolderPokemonVersionDetail](https://pokeapi.co/docs/v2#itemholderpokemonversiondetail)_ |

#### ItemHolderPokemonVersionDetail (type)

| Name | Description | Type |
| --- | --- | --- |
| rarity | How often this Pokémon holds this item in this version. | _integer_ |
| version | The version that this item is held in by the Pokémon. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |

### Item Attributes (endpoint)

Item attributes define particular aspects of items, e.g. "usable in battle" or "consumable".

GET https://pokeapi.co/api/v2/item-attribute/{id or name}/

- id:1
- name:"countable"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Has a count in the bag"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


items:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"master-ball"
    - url:"https://pokeapi.co/api/v2/item/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Countable"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.495 kB, 28 lines)

#### ItemAttribute (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| items | A list of items that have this attribute. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Item](https://pokeapi.co/docs/v2#item))_ |
| names | The name of this item attribute listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| descriptions | The description of this item attribute listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |

### Item Categories (endpoint)

Item categories determine where items will be placed in the players bag.

GET https://pokeapi.co/api/v2/item-category/{id or name}/

- id:1
- name:"stat-boosts"
- ▶


items:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"guard-spec"
    - url:"https://pokeapi.co/api/v2/item/55/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Stat boosts"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


pocket:{} 2 keys
  - name:"battle"
  - url:"https://pokeapi.co/api/v2/item-pocket/7/"

View raw JSON (0.405 kB, 23 lines)

#### ItemCategory (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| items | A list of items that are a part of this category. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Item](https://pokeapi.co/docs/v2#item))_ |
| names | The name of this item category listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pocket | The pocket items in this category would be put in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[ItemPocket](https://pokeapi.co/docs/v2#itempocket)_) |

### Item Fling Effects (endpoint)

The various effects of the move "Fling" when used with different items.

GET https://pokeapi.co/api/v2/item-fling-effect/{id or name}/

- id:1
- name:"badly-poison"
- ▶


effect\_entries:\[\] 1 item
  - ▶


    0:{} 2 keys
    - effect:"Badly poisons the target."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


items:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"toxic-orb"
    - url:"https://pokeapi.co/api/v2/item/249/"

View raw JSON (0.336 kB, 19 lines)

#### ItemFlingEffect (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| effect\_entries | The result of this fling effect listed in different languages. | list _[Effect](https://pokeapi.co/docs/v2#effect)_ |
| items | A list of items that have this fling effect. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Item](https://pokeapi.co/docs/v2#item))_ |

### Item Pockets (endpoint)

Pockets within the players bag used for storing items by category.

GET https://pokeapi.co/api/v2/item-pocket/{id or name}/

- id:1
- name:"misc"
- ▶


categories:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"collectibles"
    - url:"https://pokeapi.co/api/v2/item-category/9/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Items"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.312 kB, 19 lines)

#### ItemPocket (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| categories | A list of item categories that are relevant to this item pocket. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([ItemCategory](https://pokeapi.co/docs/v2#itemcategory))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

## Locations (group)

### Locations (endpoint)

Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.

GET https://pokeapi.co/api/v2/location/{id or name}/

- id:1
- name:"canalave-city"
- ▶


region:{} 2 keys
  - name:"sinnoh"
  - url:"https://pokeapi.co/api/v2/region/4/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Canalave City"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


game\_indices:\[\] 1 item
  - ▶


    0:{} 2 keys
    - game\_index:7
    - ▶


      generation:{} 2 keys
      - name:"generation-iv"
      - url:"https://pokeapi.co/api/v2/generation/4/"
- ▶


areas:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"canalave-city-area"
    - url:"https://pokeapi.co/api/v2/location-area/1/"

View raw JSON (0.6 kB, 32 lines)

#### Location (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| region | The region this location can be found in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Region](https://pokeapi.co/docs/v2#region)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| game\_indices | A list of game indices relevent to this location by generation. | list _[GenerationGameIndex](https://pokeapi.co/docs/v2#generationgameindex)_ |
| areas | Areas that can be found within this location. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([LocationArea](https://pokeapi.co/docs/v2#locationarea))_ |

### Location Areas (endpoint)

Location areas are sections of areas, such as floors in a building or cave. Each area has its own set of possible Pokémon encounters.

GET https://pokeapi.co/api/v2/location-area/{id or name}/

- id:1
- name:"canalave-city-area"
- game\_index:1
- ▶


encounter\_method\_rates:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      encounter\_method:{} 2 keys
      - name:"old-rod"
      - url:"https://pokeapi.co/api/v2/encounter-method/2/"
    - ▶


      version\_details:\[\] 1 item
- ▶


location:{} 2 keys
  - name:"canalave-city"
  - url:"https://pokeapi.co/api/v2/location/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:""
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


pokemon\_encounters:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      pokemon:{} 2 keys
      - name:"tentacool"
      - url:"https://pokeapi.co/api/v2/pokemon/72/"
    - ▶


      version\_details:\[\] 1 item

View raw JSON (1.405 kB, 64 lines)

#### LocationArea (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| game\_index | The internal id of an API resource within game data. | _integer_ |
| encounter\_method\_rates | A list of methods in which Pokémon may be encountered in this area and how likely the method will occur depending on the version of the game. | list _[EncounterMethodRate](https://pokeapi.co/docs/v2#encountermethodrate)_ |
| location | The region this location area can be found in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Location](https://pokeapi.co/docs/v2#location)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_encounters | A list of Pokémon that can be encountered in this area along with version specific details about the encounter. | list _[PokemonEncounter](https://pokeapi.co/docs/v2#pokemonencounter)_ |

#### EncounterMethodRate (type)

| Name | Description | Type |
| --- | --- | --- |
| encounter\_method | The method in which Pokémon may be encountered in an area.. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[EncounterMethod](https://pokeapi.co/docs/v2#encountermethod)_) |
| version\_details | The chance of the encounter to occur on a version of the game. | list _[EncounterVersionDetails](https://pokeapi.co/docs/v2#encounterversiondetails)_ |

#### EncounterVersionDetails (type)

| Name | Description | Type |
| --- | --- | --- |
| rate | The chance of an encounter to occur. | _integer_ |
| version | The version of the game in which the encounter can occur with the given chance. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |

#### PokemonEncounter (type)

| Name | Description | Type |
| --- | --- | --- |
| pokemon | The Pokémon being encountered. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |
| version\_details | A list of versions and encounters with Pokémon that might happen in the referenced location area. | list _[VersionEncounterDetail](https://pokeapi.co/docs/v2#versionencounterdetail)_ |

### Pal Park Areas (endpoint)

Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are specific to [Pal Park](https://bulbapedia.bulbagarden.net/wiki/Pal_Park).

GET https://pokeapi.co/api/v2/pal-park-area/{id or name}/

- id:1
- name:"forest"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Forest"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


pokemon\_encounters:\[\] 1 item
  - ▶


    0:{} 3 keys
    - base\_score:30
    - rate:50
    - ▶


      pokemon\_species:{} 2 keys
      - name:"caterpie"
      - url:"https://pokeapi.co/api/v2/pokemon-species/10/"

View raw JSON (0.403 kB, 23 lines)

#### PalParkArea (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_encounters | A list of Pokémon encountered in thi pal park area along with details. | list _[PalParkEncounterSpecies](https://pokeapi.co/docs/v2#palparkencounterspecies)_ |

#### PalParkEncounterSpecies (type)

| Name | Description | Type |
| --- | --- | --- |
| base\_score | The base score given to the player when this Pokémon is caught during a pal park run. | _integer_ |
| rate | The base rate for encountering this Pokémon in this pal park area. | _integer_ |
| pokemon\_species | The Pokémon species being encountered. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |

### Regions (endpoint)

A region is an organized area of the Pokémon world. Most often, the main difference between regions is the species of Pokémon that can be encountered within them.

GET https://pokeapi.co/api/v2/region/{id or name}/

- id:1
- name:"kanto"
- ▶


locations:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"celadon-city"
    - url:"https://pokeapi.co/api/v2/location/67/"
- ▶


main\_generation:{} 2 keys
  - name:"generation-i"
  - url:"https://pokeapi.co/api/v2/generation/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Kanto"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


pokedexes:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"kanto"
    - url:"https://pokeapi.co/api/v2/pokedex/2/"
- ▶


version\_groups:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"red-blue"
    - url:"https://pokeapi.co/api/v2/version-group/1/"

View raw JSON (0.649 kB, 35 lines)

#### Region (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| locations | A list of locations that can be found in this region. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Location](https://pokeapi.co/docs/v2#location))_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| main\_generation | The generation this region was introduced in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| pokedexes | A list of pokédexes that catalogue Pokémon in this region. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Pokedex](https://pokeapi.co/docs/v2#pokedex))_ |
| version\_groups | A list of version groups where this region can be visited. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([VersionGroup](https://pokeapi.co/docs/v2#versiongroup))_ |

## Machines (group)

### Machines (endpoint)

Machines are the representation of items that teach moves to Pokémon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

GET https://pokeapi.co/api/v2/machine/{id}/

- id:1
- ▶


item:{} 2 keys
  - name:"tm01"
  - url:"https://pokeapi.co/api/v2/item/305/"
- ▶


move:{} 2 keys
  - name:"mega-punch"
  - url:"https://pokeapi.co/api/v2/move/5/"
- ▶


version\_group:{} 2 keys
  - name:"red-blue"
  - url:"https://pokeapi.co/api/v2/version/1/"

View raw JSON (0.289 kB, 15 lines)

#### Machine (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| item | The TM or HM item that corresponds to this machine. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| move | The move that is taught by this machine. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Move](https://pokeapi.co/docs/v2#move)_) |
| version\_group | The version group that this machine applies to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

## Moves (group)

### Moves (endpoint)

Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.

GET https://pokeapi.co/api/v2/move/{id or name}/

- id:1
- name:"pound"
- accuracy:100
- effect\_chance:null
- pp:35
- priority:0
- power:40
- ▶


contest\_combos:{} 2 keys
  - ▶


    normal:{} 2 keys
    - ▶


      use\_before:\[\] 3 items
      - ▶


        0:{} 2 keys
        - name:"double-slap"
        - url:"https://pokeapi.co/api/v2/move/3/"
      - ▶


        1:{} 2 keys
        - name:"headbutt"
        - url:"https://pokeapi.co/api/v2/move/29/"
      - ▶


        2:{} 2 keys
        - name:"feint-attack"
        - url:"https://pokeapi.co/api/v2/move/185/"
    - use\_after:null
  - ▶


    super:{} 2 keys
    - use\_before:null
    - use\_after:null
- ▶


contest\_type:{} 2 keys
  - name:"tough"
  - url:"https://pokeapi.co/api/v2/contest-type/5/"
- ▶


contest\_effect:{} 1 key
  - url:"https://pokeapi.co/api/v2/contest-effect/1/"
- ▶


damage\_class:{} 2 keys
  - name:"physical"
  - url:"https://pokeapi.co/api/v2/move-damage-class/2/"
- ▶


effect\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - effect:"Inflicts \[regular damage\]{mechanic:regular-damage}."
    - short\_effect:"Inflicts regular damage with no additional effect."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- effect\_changes:\[\] 0 items
- ▶


generation:{} 2 keys
  - name:"generation-i"
  - url:"https://pokeapi.co/api/v2/generation/1/"
- ▶


meta:{} 12 keys
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Pound"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- past\_values:\[\] 0 items
- stat\_changes:\[\] 0 items
- ▶


super\_contest\_effect:{} 1 key
  - url:"https://pokeapi.co/api/v2/super-contest-effect/5/"
- ▶


target:{} 2 keys
  - name:"selected-pokemon"
  - url:"https://pokeapi.co/api/v2/move-target/10/"
- ▶


type:{} 2 keys
  - name:"normal"
  - url:"https://pokeapi.co/api/v2/type/1/"
- ▶


learned\_by\_pokemon:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"clefairy"
    - url:"https://pokeapi.co/api/v2/pokemon/35/"
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - flavor\_text:"Pounds with fore­
      legs or tail."
    - ▶


      language:{} 2 keys
      - url:"https://pokeapi.co/api/v2/language/9/"
      - name:"en"
    - ▶


      version\_group:{} 2 keys
      - url:"https://pokeapi.co/api/v2/version-group/3/"
      - name:"gold-silver"

View raw JSON (2.714 kB, 119 lines)

#### Move (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| accuracy | The percent value of how likely this move is to be successful. | _integer_ |
| effect\_chance | The percent value of how likely it is this moves effect will happen. | _integer_ |
| pp | Power points. The number of times this move can be used. | _integer_ |
| priority | A value between -8 and 8. Sets the order in which moves are executed during battle. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Priority) for greater detail. | _integer_ |
| power | The base power of this move with a value of 0 if it does not have a base power. | _integer_ |
| contest\_combos | A detail of normal and super contest combos that require this move. | [ContestComboSets](https://pokeapi.co/docs/v2#contestcombosets) |
| contest\_type | The type of appeal this move gives a Pokémon when used in a contest. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[ContestType](https://pokeapi.co/docs/v2#contesttype)_) |
| contest\_effect | The effect the move has when used in a contest. | _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ ( _[ContestEffect](https://pokeapi.co/docs/v2#contesteffect)_) |
| damage\_class | The type of damage the move inflicts on the target, e.g. physical. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveDamageClass](https://pokeapi.co/docs/v2#movedamageclass)_) |
| effect\_entries | The effect of this move listed in different languages. | list _[VerboseEffect](https://pokeapi.co/docs/v2#verboseeffect)_ |
| effect\_changes | The list of previous effects this move has had across version groups of the games. | list _[AbilityEffectChange](https://pokeapi.co/docs/v2#abilityeffectchange)_ |
| learned\_by\_pokemon | List of Pokemon that can learn the move | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Pokemon](https://pokeapi.co/docs/v2#pokemon))_ |
| flavor\_text\_entries | The flavor text of this move listed in different languages. | list _[MoveFlavorText](https://pokeapi.co/docs/v2#moveflavortext)_ |
| generation | The generation in which this move was introduced. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| machines | A list of the machines that teach this move. | list _[MachineVersionDetail](https://pokeapi.co/docs/v2#machineversiondetail)_ |
| meta | Metadata about this move | [MoveMetaData](https://pokeapi.co/docs/v2#movemetadata) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| past\_values | A list of move resource value changes across version groups of the game. | list _[PastMoveStatValues](https://pokeapi.co/docs/v2#pastmovestatvalues)_ |
| stat\_changes | A list of stats this moves effects and how much it effects them. | list _[MoveStatChange](https://pokeapi.co/docs/v2#movestatchange)_ |
| super\_contest\_effect | The effect the move has when used in a super contest. | _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ ( _[SuperContestEffect](https://pokeapi.co/docs/v2#supercontesteffect)_) |
| target | The type of target that will receive the effects of the attack. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveTarget](https://pokeapi.co/docs/v2#movetarget)_) |
| type | The elemental type of this move. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |

#### ContestComboSets (type)

| Name | Description | Type |
| --- | --- | --- |
| normal | A detail of moves this move can be used before or after, granting additional appeal points in contests. | [ContestComboDetail](https://pokeapi.co/docs/v2#contestcombodetail) |
| super | A detail of moves this move can be used before or after, granting additional appeal points in super contests. | [ContestComboDetail](https://pokeapi.co/docs/v2#contestcombodetail) |

#### ContestComboDetail (type)

| Name | Description | Type |
| --- | --- | --- |
| use\_before | A list of moves to use before this move. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| use\_after | A list of moves to use after this move. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |

#### MoveFlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| flavor\_text | The localized flavor text for an api resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |
| version\_group | The version group that uses this flavor text. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

#### MoveMetaData (type)

| Name | Description | Type |
| --- | --- | --- |
| ailment | The status ailment this move inflicts on its target. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveAilment](https://pokeapi.co/docs/v2#moveailment)_) |
| category | The category of move this move falls under, e.g. damage or ailment. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveCategory](https://pokeapi.co/docs/v2#movecategory)_) |
| min\_hits | The minimum number of times this move hits. Null if it always only hits once. | _integer_ |
| max\_hits | The maximum number of times this move hits. Null if it always only hits once. | _integer_ |
| min\_turns | The minimum number of turns this move continues to take effect. Null if it always only lasts one turn. | _integer_ |
| max\_turns | The maximum number of turns this move continues to take effect. Null if it always only lasts one turn. | _integer_ |
| drain | HP drain (if positive) or Recoil damage (if negative), in percent of damage done. | _integer_ |
| healing | The amount of hp gained by the attacking Pokemon, in percent of it's maximum HP. | _integer_ |
| crit\_rate | Critical hit rate bonus. | _integer_ |
| ailment\_chance | The likelihood this attack will cause an ailment. | _integer_ |
| flinch\_chance | The likelihood this attack will cause the target Pokémon to flinch. | _integer_ |
| stat\_chance | The likelihood this attack will cause a stat change in the target Pokémon. | _integer_ |

#### MoveStatChange (type)

| Name | Description | Type |
| --- | --- | --- |
| change | The amount of change. | _integer_ |
| stat | The stat being affected. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Stat](https://pokeapi.co/docs/v2#stat)_) |

#### PastMoveStatValues (type)

| Name | Description | Type |
| --- | --- | --- |
| accuracy | The percent value of how likely this move is to be successful. | _integer_ |
| effect\_chance | The percent value of how likely it is this moves effect will take effect. | _integer_ |
| power | The base power of this move with a value of 0 if it does not have a base power. | _integer_ |
| pp | Power points. The number of times this move can be used. | _integer_ |
| effect\_entries | The effect of this move listed in different languages. | list _[VerboseEffect](https://pokeapi.co/docs/v2#verboseeffect)_ |
| type | The elemental type of this move. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |
| version\_group | The version group in which these move stat values were in effect. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

### Move Ailments (endpoint)

Move Ailments are status conditions caused by moves used during battle. See [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Status_condition) for greater detail.

GET https://pokeapi.co/api/v2/move-ailment/{id or name}/

- id:1
- name:"paralysis"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"thunder-punch"
    - url:"https://pokeapi.co/api/v2/move/9/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Paralysis"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.308 kB, 19 lines)

#### MoveAilment (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| moves | A list of moves that cause this ailment. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Move Battle Styles (endpoint)

Styles of moves when used in the Battle Palace. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Battle_Frontier_(Generation_III)) for greater detail.

GET https://pokeapi.co/api/v2/move-battle-style/{id or name}/

- id:1
- name:"attack"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Attack"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.192 kB, 13 lines)

#### MoveBattleStyle (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Move Categories (endpoint)

Very general categories that loosely group move effects.

GET https://pokeapi.co/api/v2/move-category/{id or name}/

- id:1
- name:"ailment"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"No damage; inflicts status ailment"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"sing"
    - url:"https://pokeapi.co/api/v2/move/47/"

View raw JSON (0.337 kB, 19 lines)

#### MoveCategory (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| moves | A list of moves that fall into this category. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| descriptions | The description of this resource listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |

### Move Damage Classes (endpoint)

Damage classes moves can have, e.g. physical, special, or non-damaging.

GET https://pokeapi.co/api/v2/move-damage-class/{id or name}/

- id:1
- name:"status"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"ãƒ€ãƒ¡ãƒ¼ã‚¸ãªã„"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"swords-dance"
    - url:"https://pokeapi.co/api/v2/move/14/"

View raw JSON (0.349 kB, 19 lines)

#### MoveDamageClass (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| descriptions | The description of this resource listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| moves | A list of moves that fall into this damage class. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Move Learn Methods (endpoint)

Methods by which Pokémon can learn moves.

GET https://pokeapi.co/api/v2/move-learn-method/{id or name}/

- id:1
- name:"level-up"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Level up"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Wird gelernt, wenn ein Pokémon ein bestimmtes Level erreicht."
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


version\_groups:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"red-blue"
    - url:"https://pokeapi.co/api/v2/version-group/1/"

View raw JSON (0.548 kB, 28 lines)

#### MoveLearnMethod (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| descriptions | The description of this resource listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| version\_groups | A list of version groups where moves can be learned through this method. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([VersionGroup](https://pokeapi.co/docs/v2#versiongroup))_ |

### Move Targets (endpoint)

Targets moves can be directed at during battle. Targets can be Pokémon, environments or even other moves.

GET https://pokeapi.co/api/v2/move-target/{id or name}/

- id:1
- name:"specific-move"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Eine spezifische Fähigkeit. Wie diese Fähigkeit genutzt wird, hängt von den genutzten Fähigkeiten ab."
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"counter"
    - url:"https://pokeapi.co/api/v2/move/68/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Spezifische Fähigkeit"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"

View raw JSON (0.592 kB, 28 lines)

#### MoveTarget (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| descriptions | The description of this resource listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| moves | A list of moves that that are directed at this target. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

## Pokémon (group)

### Abilities (endpoint)

Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have multiple possible abilities but can have only one ability at a time. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Ability) for greater detail.

GET https://pokeapi.co/api/v2/ability/{id or name}/

- id:1
- name:"stench"
- is\_main\_series:true
- ▶


generation:{} 2 keys
  - name:"generation-iii"
  - url:"https://pokeapi.co/api/v2/generation/3/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Stench"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


effect\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - effect:"This Pokémon's damaging moves have a 10% chance to make the target \[flinch\]{mechanic:flinch} with each hit if they do not already cause flinching as a secondary effect.

      This ability does not stack with a held item.

      Overworld: The wild encounter rate is halved while this Pokémon is first in the party."
    - short\_effect:"Has a 10% chance of making target Pokémon \[flinch\]{mechanic:flinch} with each hit."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


effect\_changes:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      version\_group:{} 2 keys
      - name:"black-white"
      - url:"https://pokeapi.co/api/v2/version-group/11/"
    - ▶


      effect\_entries:\[\] 1 item
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - flavor\_text:"è‡­ãã¦ã€€ç›¸æ‰‹ãŒ
      ã²ã‚‹ã‚€ã€€ã“ã¨ãŒã‚ã‚‹ã€‚"
    - ▶


      language:{} 2 keys
      - name:"ja-kanji"
      - url:"https://pokeapi.co/api/v2/language/11/"
    - ▶


      version\_group:{} 2 keys
      - name:"x-y"
      - url:"https://pokeapi.co/api/v2/version-group/15/"
- ▶


pokemon:\[\] 1 item
  - ▶


    0:{} 3 keys
    - is\_hidden:true
    - slot:3
    - ▶


      pokemon:{} 2 keys
      - name:"gloom"
      - url:"https://pokeapi.co/api/v2/pokemon/44/"

View raw JSON (1.896 kB, 68 lines)

#### Ability (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| is\_main\_series | Whether or not this ability originated in the main series of the video games. | _boolean_ |
| generation | The generation this ability originated in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| effect\_entries | The effect of this ability listed in different languages. | list _[VerboseEffect](https://pokeapi.co/docs/v2#verboseeffect)_ |
| effect\_changes | The list of previous effects this ability has had across version groups. | list _[AbilityEffectChange](https://pokeapi.co/docs/v2#abilityeffectchange)_ |
| flavor\_text\_entries | The flavor text of this ability listed in different languages. | list _[AbilityFlavorText](https://pokeapi.co/docs/v2#abilityflavortext)_ |
| pokemon | A list of Pokémon that could potentially have this ability. | list _[AbilityPokemon](https://pokeapi.co/docs/v2#abilitypokemon)_ |

#### AbilityEffectChange (type)

| Name | Description | Type |
| --- | --- | --- |
| effect\_entries | The previous effect of this ability listed in different languages. | list _[Effect](https://pokeapi.co/docs/v2#effect)_ |
| version\_group | The version group in which the previous effect of this ability originated. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

#### AbilityFlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| flavor\_text | The localized name for an API resource in a specific language. | _string_ |
| language | The language this text resource is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |
| version\_group | The version group that uses this flavor text. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

#### AbilityPokemon (type)

| Name | Description | Type |
| --- | --- | --- |
| is\_hidden | Whether or not this a hidden ability for the referenced Pokémon. | _boolean_ |
| slot | Pokémon have 3 ability 'slots' which hold references to possible abilities they could have. This is the slot of this ability for the referenced pokemon. | _integer_ |
| pokemon | The Pokémon this ability could belong to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |

### Characteristics (endpoint)

Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene\_modulo). Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Characteristic) for greater detail.

GET https://pokeapi.co/api/v2/characteristic/{id}/

- id:1
- gene\_modulo:0
- ▶


possible\_values:\[\] 7 items
- ▶


highest\_stat:{} 2 keys
  - name:"hp"
  - url:"https://pokeapi.co/api/v2/stat/1/"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Loves to eat"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.383 kB, 26 lines)

#### Characteristic (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| gene\_modulo | The remainder of the highest stat/IV divided by 5. | _integer_ |
| possible\_values | The possible values of the highest stat that would result in a Pokémon recieving this characteristic when divided by 5. | list _integer_ |
| highest\_stat | The stat which results in this characteristic. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Stat](https://pokeapi.co/docs/v2#stat)_) |
| descriptions | The descriptions of this characteristic listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |

### Egg Groups (endpoint)

Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may belong to either one or two Egg Groups. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Egg_Group) for greater detail.

GET https://pokeapi.co/api/v2/egg-group/{id or name}/

- id:1
- name:"monster"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"かいじゅう"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"bulbasaur"
    - url:"https://pokeapi.co/api/v2/pokemon-species/1/"

View raw JSON (0.329 kB, 19 lines)

#### EggGroup (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_species | A list of all Pokémon species that are members of this egg group. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

### Genders (endpoint)

Genders were introduced in Generation II for the purposes of breeding Pokémon but can also result in visual differences or even different evolutionary lines. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Gender) for greater detail.

GET https://pokeapi.co/api/v2/gender/{id or name}/

- id:1
- name:"female"
- ▶


pokemon\_species\_details:\[\] 1 item
  - ▶


    0:{} 2 keys
    - rate:1
    - ▶


      pokemon\_species:{} 2 keys
      - name:"bulbasaur"
      - url:"https://pokeapi.co/api/v2/pokemon-species/1/"
- ▶


required\_for\_evolution:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"wormadam"
    - url:"https://pokeapi.co/api/v2/pokemon-species/413/"

View raw JSON (0.359 kB, 19 lines)

#### Gender (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| pokemon\_species\_details | A list of Pokémon species that can be this gender and how likely it is that they will be. | list _[PokemonSpeciesGender](https://pokeapi.co/docs/v2#pokemonspeciesgender)_ |
| required\_for\_evolution | A list of Pokémon species that required this gender in order for a Pokémon to evolve into them. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

#### PokemonSpeciesGender (type)

| Name | Description | Type |
| --- | --- | --- |
| rate | The chance of this Pokémon being female, in eighths; or -1 for genderless. | _integer_ |
| pokemon\_species | A Pokémon species that can be the referenced gender. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |

### Growth Rates (endpoint)

Growth rates are the speed with which Pokémon gain levels through experience. Check out [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Experience) for greater detail.

GET https://pokeapi.co/api/v2/growth-rate/{id or name}/

- id:1
- name:"slow"
- formula:"\\frac{5x^3}{4}"
- ▶


descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"langsam"
    - ▶


      language:{} 2 keys
      - name:"de"
      - url:"https://pokeapi.co/api/v2/language/6/"
- ▶


levels:\[\] 1 item
  - ▶


    0:{} 2 keys
    - level:100
    - experience:1250000
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"growlithe"
    - url:"https://pokeapi.co/api/v2/pokemon-species/58/"

View raw JSON (0.444 kB, 26 lines)

#### GrowthRate (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| formula | The formula used to calculate the rate at which the Pokémon species gains level. | _string_ |
| descriptions | The descriptions of this characteristic listed in different languages. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| levels | A list of levels and the amount of experienced needed to atain them based on this growth rate. | list _[GrowthRateExperienceLevel](https://pokeapi.co/docs/v2#growthrateexperiencelevel)_ |
| pokemon\_species | A list of Pokémon species that gain levels at this growth rate. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

#### GrowthRateExperienceLevel (type)

| Name | Description | Type |
| --- | --- | --- |
| level | The level gained. | _integer_ |
| experience | The amount of experience required to reach the referenced level. | _integer_ |

### Natures (endpoint)

Natures influence how a Pokémon's stats grow. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Nature) for greater detail.

GET https://pokeapi.co/api/v2/nature/{id or name}/

- id:2
- name:"bold"
- ▶


decreased\_stat:{} 2 keys
  - name:"attack"
  - url:"https://pokeapi.co/api/v2/stat/2/"
- ▶


increased\_stat:{} 2 keys
  - name:"defense"
  - url:"https://pokeapi.co/api/v2/stat/3/"
- ▶


likes\_flavor:{} 2 keys
  - name:"sour"
  - url:"https://pokeapi.co/api/v2/berry-flavor/5/"
- ▶


hates\_flavor:{} 2 keys
  - name:"spicy"
  - url:"https://pokeapi.co/api/v2/berry-flavor/1/"
- ▶


pokeathlon\_stat\_changes:\[\] 1 item
  - ▶


    0:{} 2 keys
    - max\_change:-2
    - ▶


      pokeathlon\_stat:{} 2 keys
      - name:"speed"
      - url:"https://pokeapi.co/api/v2/pokeathlon-stat/1/"
- ▶


move\_battle\_style\_preferences:\[\] 1 item
  - ▶


    0:{} 3 keys
    - low\_hp\_preference:32
    - high\_hp\_preference:30
    - ▶


      move\_battle\_style:{} 2 keys
      - name:"attack"
      - url:"https://pokeapi.co/api/v2/move-battle-style/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"がんばりや"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"

View raw JSON (1.031 kB, 48 lines)

#### Nature (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| decreased\_stat | The stat decreased by 10% in Pokémon with this nature. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Stat](https://pokeapi.co/docs/v2#stat)_) |
| increased\_stat | The stat increased by 10% in Pokémon with this nature. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Stat](https://pokeapi.co/docs/v2#stat)_) |
| hates\_flavor | The flavor hated by Pokémon with this nature. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[BerryFlavor](https://pokeapi.co/docs/v2#berryflavor)_) |
| likes\_flavor | The flavor liked by Pokémon with this nature. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[BerryFlavor](https://pokeapi.co/docs/v2#berryflavor)_) |
| pokeathlon\_stat\_changes | A list of Pokéathlon stats this nature effects and how much it effects them. | list _[NatureStatChange](https://pokeapi.co/docs/v2#naturestatchange)_ |
| move\_battle\_style\_preferences | A list of battle styles and how likely a Pokémon with this nature is to use them in the Battle Palace or Battle Tent. | list _[MoveBattleStylePreference](https://pokeapi.co/docs/v2#movebattlestylepreference)_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

#### NatureStatChange (type)

| Name | Description | Type |
| --- | --- | --- |
| max\_change | The amount of change. | _integer_ |
| pokeathlon\_stat | The stat being affected. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokeathlonStat](https://pokeapi.co/docs/v2#pokeathlonstat)_) |

#### MoveBattleStylePreference (type)

| Name | Description | Type |
| --- | --- | --- |
| low\_hp\_preference | Chance of using the move, in percent, if HP is under one half. | _integer_ |
| high\_hp\_preference | Chance of using the move, in percent, if HP is over one half. | _integer_ |
| move\_battle\_style | The move battle style. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveBattleStyle](https://pokeapi.co/docs/v2#movebattlestyle)_) |

### Pokeathlon Stats (endpoint)

Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In Pokéathlons, competitions happen on different courses; one for each of the different Pokéathlon stats. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9athlon) for greater detail.

GET https://pokeapi.co/api/v2/pokeathlon-stat/{id or name}/

- id:1
- name:"speed"
- ▶


affecting\_natures:{} 2 keys
  - ▶


    increase:\[\] 1 item
    - ▶


      0:{} 2 keys
      - max\_change:2
      - ▶


        nature:{} 2 keys
        - name:"timid"
        - url:"https://pokeapi.co/api/v2/nature/5/"
  - ▶


    decrease:\[\] 1 item
    - ▶


      0:{} 2 keys
      - max\_change:-1
      - ▶


        nature:{} 2 keys
        - name:"hardy"
        - url:"https://pokeapi.co/api/v2/nature/1/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Speed"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.576 kB, 33 lines)

#### PokeathlonStat (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| affecting\_natures | A detail of natures which affect this Pokéathlon stat positively or negatively. | [NaturePokeathlonStatAffectSets](https://pokeapi.co/docs/v2#naturepokeathlonstataffectsets) |

#### NaturePokeathlonStatAffectSets (type)

| Name | Description | Type |
| --- | --- | --- |
| increase | A list of natures and how they change the referenced Pokéathlon stat. | list _[NaturePokeathlonStatAffect](https://pokeapi.co/docs/v2#naturepokeathlonstataffect)_ |
| decrease | A list of natures and how they change the referenced Pokéathlon stat. | list _[NaturePokeathlonStatAffect](https://pokeapi.co/docs/v2#naturepokeathlonstataffect)_ |

#### NaturePokeathlonStatAffect (type)

| Name | Description | Type |
| --- | --- | --- |
| max\_change | The maximum amount of change to the referenced Pokéathlon stat. | _integer_ |
| nature | The nature causing the change. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Nature](https://pokeapi.co/docs/v2#nature)_) |

### Pokemon (endpoint)

Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a specific species but may take on a variant which makes it differ from other Pokémon of the same species, such as base stats, available abilities and typings. See [Bulbapedia](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_(species)) for greater detail.

GET https://pokeapi.co/api/v2/pokemon/{id or name}/

- id:35
- name:"clefairy"
- base\_experience:113
- height:6
- is\_default:true
- order:56
- weight:75
- ▶


abilities:\[\] 1 item
  - ▶


    0:{} 3 keys
    - is\_hidden:true
    - slot:3
    - ▶


      ability:{} 2 keys
      - name:"friend-guard"
      - url:"https://pokeapi.co/api/v2/ability/132/"
- ▶


forms:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"clefairy"
    - url:"https://pokeapi.co/api/v2/pokemon-form/35/"
- ▶


game\_indices:\[\] 1 item
  - ▶


    0:{} 2 keys
    - game\_index:35
    - ▶


      version:{} 2 keys
      - name:"white-2"
      - url:"https://pokeapi.co/api/v2/version/22/"
- ▶


held\_items:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      item:{} 2 keys
      - name:"moon-stone"
      - url:"https://pokeapi.co/api/v2/item/81/"
    - ▶


      version\_details:\[\] 1 item
- location\_area\_encounters:"/api/v2/pokemon/35/encounters"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      move:{} 2 keys
      - name:"pound"
      - url:"https://pokeapi.co/api/v2/move/1/"
    - ▶


      version\_group\_details:\[\] 1 item
- ▶


species:{} 2 keys
  - name:"clefairy"
  - url:"https://pokeapi.co/api/v2/pokemon-species/35/"
- ▶


sprites:{} 10 keys
- ▶


cries:{} 2 keys
  - latest:"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/35.ogg"
  - legacy:"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/35.ogg"
- ▶


stats:\[\] 1 item
  - ▶


    0:{} 3 keys
    - base\_stat:35
    - effort:0
    - ▶


      stat:{} 2 keys
      - name:"speed"
      - url:"https://pokeapi.co/api/v2/stat/6/"
- ▶


types:\[\] 1 item
  - ▶


    0:{} 2 keys
    - slot:1
    - ▶


      type:{} 2 keys
      - name:"fairy"
      - url:"https://pokeapi.co/api/v2/type/18/"
- ▶


past\_types:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      generation:{} 2 keys
      - name:"generation-v"
      - url:"https://pokeapi.co/api/v2/generation/5/"
    - ▶


      types:\[\] 1 item
- ▶


past\_abilities:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      generation:{} 2 keys
      - name:"generation-iv"
      - url:"https://pokeapi.co/api/v2/generation/4/"
    - ▶


      abilities:\[\] 1 item

View raw JSON (15.38 kB, 309 lines)

#### Pokemon (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| base\_experience | The base experience gained for defeating this Pokémon. | _integer_ |
| height | The height of this Pokémon in decimetres. | _integer_ |
| is\_default | Set for exactly one Pokémon used as the default for each species. | _boolean_ |
| order | Order for sorting. Almost national order, except families are grouped together. | _integer_ |
| weight | The weight of this Pokémon in hectograms. | _integer_ |
| abilities | A list of abilities this Pokémon could potentially have. | list _[PokemonAbility](https://pokeapi.co/docs/v2#pokemonability)_ |
| forms | A list of forms this Pokémon can take on. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonForm](https://pokeapi.co/docs/v2#pokemonform))_ |
| game\_indices | A list of game indices relevent to Pokémon item by generation. | list _[VersionGameIndex](https://pokeapi.co/docs/v2#versiongameindex)_ |
| held\_items | A list of items this Pokémon may be holding when encountered. | list _[PokemonHeldItem](https://pokeapi.co/docs/v2#pokemonhelditem)_ |
| location\_area\_encounters | A link to a list of location areas, as well as encounter details pertaining to specific versions. | _string_ |
| moves | A list of moves along with learn methods and level details pertaining to specific version groups. | list _[PokemonMove](https://pokeapi.co/docs/v2#pokemonmove)_ |
| past\_types | A list of details showing types this pokémon had in previous generations | list _[PokemonTypePast](https://pokeapi.co/docs/v2#pokemontypepast)_ |
| past\_abilities | A list of details showing abilities this pokémon had in previous generations | list _[PokemonAbilityPast](https://pokeapi.co/docs/v2#pokemonabilitypast)_ |
| past\_stats | A list of details showing stats this pokémon had in previous generations | list _[PokemonStatPast](https://pokeapi.co/docs/v2#pokemonstatpast)_ |
| sprites | A set of sprites used to depict this Pokémon in the game. A visual representation of the various sprites can be found at [PokeAPI/sprites](https://github.com/PokeAPI/sprites#sprites) | [PokemonSprites](https://pokeapi.co/docs/v2#pokemonsprites) |
| cries | A set of cries used to depict this Pokémon in the game. A visual representation of the various cries can be found at [PokeAPI/cries](https://github.com/PokeAPI/cries#cries) | [PokemonCries](https://pokeapi.co/docs/v2#pokemoncries) |
| species | The species this Pokémon belongs to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |
| stats | A list of base stat values for this Pokémon. | list _[PokemonStat](https://pokeapi.co/docs/v2#pokemonstat)_ |
| types | A list of details showing types this Pokémon has. | list _[PokemonType](https://pokeapi.co/docs/v2#pokemontype)_ |

#### PokemonAbility (type)

| Name | Description | Type |
| --- | --- | --- |
| is\_hidden | Whether or not this is a hidden ability. | _boolean_ |
| slot | The slot this ability occupies in this Pokémon species. | _integer_ |
| ability | The ability the Pokémon may have. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Ability](https://pokeapi.co/docs/v2#ability)_) |

#### PokemonType (type)

| Name | Description | Type |
| --- | --- | --- |
| slot | The order the Pokémon's types are listed in. | _integer_ |
| type | The type the referenced Pokémon has. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |

#### PokemonFormType (type)

| Name | Description | Type |
| --- | --- | --- |
| slot | The order the Pokémon's types are listed in. | _integer_ |
| type | The type the referenced Form has. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Type](https://pokeapi.co/docs/v2#type)_) |

#### PokemonTypePast (type)

| Name | Description | Type |
| --- | --- | --- |
| generation | The last generation in which the referenced pokémon had the listed types. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| types | The types the referenced pokémon had up to and including the listed generation. | list _[PokemonType](https://pokeapi.co/docs/v2#pokemontype)_ |

#### PokemonAbilityPast (type)

| Name | Description | Type |
| --- | --- | --- |
| generation | The last generation in which the referenced pokémon had the listed abilities. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| abilities | The abilities the referenced pokémon had up to and including the listed generation. If null, the slot was previously empty. | list _[PokemonAbility](https://pokeapi.co/docs/v2#pokemonability)_ |

#### PokemonStatPast (type)

| Name | Description | Type |
| --- | --- | --- |
| generation | The last generation in which the referenced pokémon had the listed stats. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| stats | The stat the Pokémon had up to and including the listed generation. | list _[PokemonStat](https://pokeapi.co/docs/v2#pokemonstat)_ |

#### PokemonHeldItem (type)

| Name | Description | Type |
| --- | --- | --- |
| item | The item the referenced Pokémon holds. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Item](https://pokeapi.co/docs/v2#item)_) |
| version\_details | The details of the different versions in which the item is held. | list _[PokemonHeldItemVersion](https://pokeapi.co/docs/v2#pokemonhelditemversion)_ |

#### PokemonHeldItemVersion (type)

| Name | Description | Type |
| --- | --- | --- |
| version | The version in which the item is held. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |
| rarity | How often the item is held. | _integer_ |

#### PokemonMove (type)

| Name | Description | Type |
| --- | --- | --- |
| move | The move the Pokémon can learn. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Move](https://pokeapi.co/docs/v2#move)_) |
| version\_group\_details | The details of the version in which the Pokémon can learn the move. | list _[PokemonMoveVersion](https://pokeapi.co/docs/v2#pokemonmoveversion)_ |

#### PokemonMoveVersion (type)

| Name | Description | Type |
| --- | --- | --- |
| move\_learn\_method | The method by which the move is learned. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveLearnMethod](https://pokeapi.co/docs/v2#movelearnmethod)_) |
| version\_group | The version group in which the move is learned. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |
| level\_learned\_at | The minimum level to learn the move. | _integer_ |
| order | Order by which the pokemon will learn the move. A newly learnt move will replace the move with lowest order. | _integer_ |

#### PokemonStat (type)

| Name | Description | Type |
| --- | --- | --- |
| stat | The stat the Pokémon has. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Stat](https://pokeapi.co/docs/v2#stat)_) |
| effort | The effort points (EV) the Pokémon has in the stat. | _integer_ |
| base\_stat | The base value of the stat. | _integer_ |

#### PokemonSprites (type)

| Name | Description | Type |
| --- | --- | --- |
| front\_default | The default depiction of this Pokémon from the front in battle. | _string_ |
| front\_shiny | The shiny depiction of this Pokémon from the front in battle. | _string_ |
| front\_female | The female depiction of this Pokémon from the front in battle. | _string_ |
| front\_shiny\_female | The shiny female depiction of this Pokémon from the front in battle. | _string_ |
| back\_default | The default depiction of this Pokémon from the back in battle. | _string_ |
| back\_shiny | The shiny depiction of this Pokémon from the back in battle. | _string_ |
| back\_female | The female depiction of this Pokémon from the back in battle. | _string_ |
| back\_shiny\_female | The shiny female depiction of this Pokémon from the back in battle. | _string_ |

#### PokemonCries (type)

| Name | Description | Type |
| --- | --- | --- |
| latest | The latest depiction of this Pokémon's cry. | _string_ |
| legacy | The legacy depiction of this Pokémon's cry. | _string_ |

### Pokemon Location Areas (endpoint)

Pokémon Location Areas are ares where Pokémon can be found.

GET https://pokeapi.co/api/v2/pokemon/{id or name}/encounters

- ▶


0:{} 2 keys
  - ▶


    location\_area:{} 2 keys
    - name:"kanto-route-2-south-towards-viridian-city"
    - url:"https://pokeapi.co/api/v2/location-area/296/"
  - ▶


    version\_details:\[\] 1 item

View raw JSON (0.837 kB, 34 lines)

#### LocationAreaEncounter (type)

| Name | Description | Type |
| --- | --- | --- |
| location\_area | The location area the referenced Pokémon can be encountered in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[LocationArea](https://pokeapi.co/docs/v2#locationarea)_) |
| version\_details | A list of versions and encounters with the referenced Pokémon that might happen. | list _[VersionEncounterDetail](https://pokeapi.co/docs/v2#versionencounterdetail)_ |

### Pokemon Colors (endpoint)

Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that are primarily orange are listed as red or brown.

GET https://pokeapi.co/api/v2/pokemon-color/{id or name}/

- id:1
- name:"black"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"é»’ã„"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"snorlax"
    - url:"https://pokeapi.co/api/v2/pokemon-species/143/"

View raw JSON (0.326 kB, 19 lines)

#### PokemonColor (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_species | A list of the Pokémon species that have this color. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

### Pokemon Forms (endpoint)

Some Pokémon may appear in one of multiple, visually different forms. These differences are purely cosmetic. For variations within a Pokémon species, which do differ in more than just visuals, the 'Pokémon' entity is used to represent such a variety.

GET https://pokeapi.co/api/v2/pokemon-form/{id or name}/

- id:10041
- name:"arceus-bug"
- order:631
- form\_order:7
- is\_default:false
- is\_battle\_only:false
- is\_mega:false
- form\_name:"bug"
- ▶


pokemon:{} 2 keys
  - name:"arceus"
  - url:"https://pokeapi.co/api/v2/pokemon/493/"
- ▶


sprites:{} 8 keys
- ▶


types:\[\] 1 item
  - ▶


    0:{} 2 keys
    - slot:1
    - ▶


      type:{} 2 keys
      - name:"bug"
      - url:"https://pokeapi.co/api/v2/type/7/"
- ▶


version\_group:{} 2 keys
  - name:"diamond-pearl"
  - url:"https://pokeapi.co/api/v2/version-group/8/"

View raw JSON (1.103 kB, 37 lines)

#### PokemonForm (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| order | The order in which forms should be sorted within all forms. Multiple forms may have equal order, in which case they should fall back on sorting by name. | _integer_ |
| form\_order | The order in which forms should be sorted within a species' forms. | _integer_ |
| is\_default | True for exactly one form used as the default for each Pokémon. | _boolean_ |
| is\_battle\_only | Whether or not this form can only happen during battle. | _boolean_ |
| is\_mega | Whether or not this form requires mega evolution. | _boolean_ |
| form\_name | The name of this form. | _string_ |
| pokemon | The Pokémon that can take on this form. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |
| types | A list of details showing types this Pokémon form has. | list _[PokemonFormType](https://pokeapi.co/docs/v2#pokemonformtype)_ |
| sprites | A set of sprites used to depict this Pokémon form in the game. | [PokemonFormSprites](https://pokeapi.co/docs/v2#pokemonformsprites) |
| version\_group | The version group this Pokémon form was introduced in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |
| names | The form specific full name of this Pokémon form, or empty if the form does not have a specific name. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| form\_names | The form specific form name of this Pokémon form, or empty if the form does not have a specific name. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

#### PokemonFormSprites (type)

| Name | Description | Type |
| --- | --- | --- |
| front\_default | The default depiction of this Pokémon form from the front in battle. | _string_ |
| front\_shiny | The shiny depiction of this Pokémon form from the front in battle. | _string_ |
| back\_default | The default depiction of this Pokémon form from the back in battle. | _string_ |
| back\_shiny | The shiny depiction of this Pokémon form from the back in battle. | _string_ |

### Pokemon Habitats (endpoint)

Habitats are generally different terrain Pokémon can be found in but can also be areas designated for rare or legendary Pokémon.

GET https://pokeapi.co/api/v2/pokemon-habitat/{id or name}/

- id:1
- name:"cave"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"grottes"
    - ▶


      language:{} 2 keys
      - name:"fr"
      - url:"https://pokeapi.co/api/v2/language/5/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"zubat"
    - url:"https://pokeapi.co/api/v2/pokemon-species/41/"

View raw JSON (0.315 kB, 19 lines)

#### PokemonHabitat (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_species | A list of the Pokémon species that can be found in this habitat. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

### Pokemon Shapes (endpoint)

Shapes used for sorting Pokémon in a Pokédex.

GET https://pokeapi.co/api/v2/pokemon-shape/{id or name}/

- id:1
- name:"ball"
- ▶


awesome\_names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - awesome\_name:"Pomaceous"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Ball"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


pokemon\_species:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"shellder"
    - url:"https://pokeapi.co/api/v2/pokemon-species/90/"

View raw JSON (0.493 kB, 28 lines)

#### PokemonShape (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| awesome\_names | The "scientific" name of this Pokémon shape listed in different languages. | list _[AwesomeName](https://pokeapi.co/docs/v2#awesomename)_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon\_species | A list of the Pokémon species that have this shape. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies))_ |

#### AwesomeName (type)

| Name | Description | Type |
| --- | --- | --- |
| awesome\_name | The localized "scientific" name for an API resource in a specific language. | _string_ |
| language | The language this "scientific" name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

### Pokemon Species (endpoint)

A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant.

GET https://pokeapi.co/api/v2/pokemon-species/{id or name}/

- id:413
- name:"wormadam"
- order:441
- gender\_rate:8
- capture\_rate:45
- base\_happiness:70
- is\_baby:false
- is\_legendary:false
- is\_mythical:false
- hatch\_counter:15
- has\_gender\_differences:false
- forms\_switchable:false
- ▶


growth\_rate:{} 2 keys
  - name:"medium"
  - url:"https://pokeapi.co/api/v2/growth-rate/2/"
- ▶


pokedex\_numbers:\[\] 1 item
  - ▶


    0:{} 2 keys
    - entry\_number:45
    - ▶


      pokedex:{} 2 keys
      - name:"kalos-central"
      - url:"https://pokeapi.co/api/v2/pokedex/12/"
- ▶


egg\_groups:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"bug"
    - url:"https://pokeapi.co/api/v2/egg-group/3/"
- ▶


color:{} 2 keys
  - name:"gray"
  - url:"https://pokeapi.co/api/v2/pokemon-color/4/"
- ▶


shape:{} 2 keys
  - name:"squiggle"
  - url:"https://pokeapi.co/api/v2/pokemon-shape/2/"
- ▶


evolves\_from\_species:{} 2 keys
  - name:"burmy"
  - url:"https://pokeapi.co/api/v2/pokemon-species/412/"
- ▶


evolution\_chain:{} 1 key
  - url:"https://pokeapi.co/api/v2/evolution-chain/213/"
- habitat:null
- ▶


generation:{} 2 keys
  - name:"generation-iv"
  - url:"https://pokeapi.co/api/v2/generation/4/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Wormadam"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


flavor\_text\_entries:\[\] 1 item
  - ▶


    0:{} 3 keys
    - flavor\_text:"When the bulb on
      its back grows
      large, it appearsto lose the
      ability to stand
      on its hind legs."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
    - ▶


      version:{} 2 keys
      - name:"red"
      - url:"https://pokeapi.co/api/v2/version/1/"
- ▶


form\_descriptions:\[\] 1 item
  - ▶


    0:{} 2 keys
    - description:"Forms have different stats and movepools. During evolution, Burmy's current cloak becomes Wormadam's form, and can no longer be changed."
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


genera:\[\] 1 item
  - ▶


    0:{} 2 keys
    - genus:"Bagworm"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"
- ▶


varieties:\[\] 1 item
  - ▶


    0:{} 2 keys
    - is\_default:true
    - ▶


      pokemon:{} 2 keys
      - name:"wormadam-plant"
      - url:"https://pokeapi.co/api/v2/pokemon/413/"

View raw JSON (2.373 kB, 102 lines)

#### PokemonSpecies (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| order | The order in which species should be sorted. Based on National Dex order, except families are grouped together and sorted by stage. | _integer_ |
| gender\_rate | The chance of this Pokémon being female, in eighths; or -1 for genderless. | _integer_ |
| capture\_rate | The base capture rate; up to 255. The higher the number, the easier the catch. | _integer_ |
| base\_happiness | The happiness when caught by a normal Pokéball; up to 255. The higher the number, the happier the Pokémon. | _integer_ |
| is\_baby | Whether or not this is a baby Pokémon. | _boolean_ |
| is\_legendary | Whether or not this is a legendary Pokémon. | _boolean_ |
| is\_mythical | Whether or not this is a mythical Pokémon. | _boolean_ |
| hatch\_counter | Initial hatch counter: one must walk Y × (hatch\_counter + 1) steps before this Pokémon's egg hatches, unless utilizing bonuses like Flame Body's. Y varies per generation. In Generations II, III, and VII, Egg cycles are 256 steps long. In Generation IV, Egg cycles are 255 steps long. In Pokémon Brilliant Diamond and Shining Pearl, Egg cycles are also 255 steps long, but are shorter on special dates. In Generations V and VI, Egg cycles are 257 steps long. In Pokémon Sword and Shield, and in Pokémon Scarlet and Violet, Egg cycles are 128 steps long. | _integer_ |
| has\_gender\_differences | Whether or not this Pokémon has visual gender differences. | _boolean_ |
| forms\_switchable | Whether or not this Pokémon has multiple forms and can switch between them. | _boolean_ |
| growth\_rate | The rate at which this Pokémon species gains levels. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[GrowthRate](https://pokeapi.co/docs/v2#growthrate)_) |
| pokedex\_numbers | A list of Pokedexes and the indexes reserved within them for this Pokémon species. | list _[PokemonSpeciesDexEntry](https://pokeapi.co/docs/v2#pokemonspeciesdexentry)_ |
| egg\_groups | A list of egg groups this Pokémon species is a member of. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([EggGroup](https://pokeapi.co/docs/v2#egggroup))_ |
| color | The color of this Pokémon for Pokédex search. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonColor](https://pokeapi.co/docs/v2#pokemoncolor)_) |
| shape | The shape of this Pokémon for Pokédex search. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonShape](https://pokeapi.co/docs/v2#pokemonshape)_) |
| evolves\_from\_species | The Pokémon species that evolves into this Pokemon\_species. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonSpecies](https://pokeapi.co/docs/v2#pokemonspecies)_) |
| evolution\_chain | The evolution chain this Pokémon species is a member of. | _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ ( _[EvolutionChain](https://pokeapi.co/docs/v2#evolutionchain)_) |
| habitat | The habitat this Pokémon species can be encountered in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PokemonHabitat](https://pokeapi.co/docs/v2#pokemonhabitat)_) |
| generation | The generation this Pokémon species was introduced in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pal\_park\_encounters | A list of encounters that can be had with this Pokémon species in pal park. | list _[PalParkEncounterArea](https://pokeapi.co/docs/v2#palparkencounterarea)_ |
| flavor\_text\_entries | A list of flavor text entries for this Pokémon species. | list _[FlavorText](https://pokeapi.co/docs/v2#flavortext)_ |
| form\_descriptions | Descriptions of different forms Pokémon take on within the Pokémon species. | list _[Description](https://pokeapi.co/docs/v2#description)_ |
| genera | The genus of this Pokémon species listed in multiple languages. | list _[Genus](https://pokeapi.co/docs/v2#genus)_ |
| varieties | A list of the Pokémon that exist within this Pokémon species. | list _[PokemonSpeciesVariety](https://pokeapi.co/docs/v2#pokemonspeciesvariety)_ |

#### Genus (type)

| Name | Description | Type |
| --- | --- | --- |
| genus | The localized genus for the referenced Pokémon species | _string_ |
| language | The language this genus is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

#### PokemonSpeciesDexEntry (type)

| Name | Description | Type |
| --- | --- | --- |
| entry\_number | The index number within the Pokédex. | _integer_ |
| pokedex | The Pokédex the referenced Pokémon species can be found in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokedex](https://pokeapi.co/docs/v2#pokedex)_) |

#### PalParkEncounterArea (type)

| Name | Description | Type |
| --- | --- | --- |
| base\_score | The base score given to the player when the referenced Pokémon is caught during a pal park run. | _integer_ |
| rate | The base rate for encountering the referenced Pokémon in this pal park area. | _integer_ |
| area | The pal park area where this encounter happens. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[PalParkArea](https://pokeapi.co/docs/v2#palparkarea)_) |

#### PokemonSpeciesVariety (type)

| Name | Description | Type |
| --- | --- | --- |
| is\_default | Whether this variety is the default variety. | _boolean_ |
| pokemon | The Pokémon variety. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |

### Stats (endpoint)

Stats determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

GET https://pokeapi.co/api/v2/stat/{id or name}/

- id:2
- name:"attack"
- game\_index:2
- is\_battle\_only:false
- ▶


affecting\_moves:{} 2 keys
  - ▶


    increase:\[\] 1 item
    - ▶


      0:{} 2 keys
      - change:2
      - ▶


        move:{} 2 keys
        - name:"swords-dance"
        - url:"https://pokeapi.co/api/v2/move/14/"
  - ▶


    decrease:\[\] 1 item
    - ▶


      0:{} 2 keys
      - change:-1
      - ▶


        move:{} 2 keys
        - name:"growl"
        - url:"https://pokeapi.co/api/v2/move/45/"
- ▶


affecting\_natures:{} 2 keys
  - ▶


    increase:\[\] 1 item
    - ▶


      0:{} 2 keys
      - name:"lonely"
      - url:"https://pokeapi.co/api/v2/nature/6/"
  - ▶


    decrease:\[\] 1 item
    - ▶


      0:{} 2 keys
      - name:"bold"
      - url:"https://pokeapi.co/api/v2/nature/2/"
- ▶


characteristics:\[\] 1 item
  - ▶


    0:{} 1 key
    - url:"https://pokeapi.co/api/v2/characteristic/2/"
- ▶


move\_damage\_class:{} 2 keys
  - name:"physical"
  - url:"https://pokeapi.co/api/v2/move-damage-class/2/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"ã“ã†ã’ã"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"

View raw JSON (1.116 kB, 58 lines)

#### Stat (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| game\_index | ID the games use for this stat. | _integer_ |
| is\_battle\_only | Whether this stat only exists within a battle. | _boolean_ |
| affecting\_moves | A detail of moves which affect this stat positively or negatively. | [MoveStatAffectSets](https://pokeapi.co/docs/v2#movestataffectsets) |
| affecting\_natures | A detail of natures which affect this stat positively or negatively. | [NatureStatAffectSets](https://pokeapi.co/docs/v2#naturestataffectsets) |
| characteristics | A list of characteristics that are set on a Pokémon when its highest base stat is this stat. | list _[APIResource](https://pokeapi.co/docs/v2#apiresource) ([Characteristic](https://pokeapi.co/docs/v2#characteristic))_ |
| move\_damage\_class | The class of damage this stat is directly related to. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveDamageClass](https://pokeapi.co/docs/v2#movedamageclass)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

#### MoveStatAffectSets (type)

| Name | Description | Type |
| --- | --- | --- |
| increase | A list of moves and how they change the referenced stat. | list _[MoveStatAffect](https://pokeapi.co/docs/v2#movestataffect)_ |
| decrease | A list of moves and how they change the referenced stat. | list _[MoveStatAffect](https://pokeapi.co/docs/v2#movestataffect)_ |

#### MoveStatAffect (type)

| Name | Description | Type |
| --- | --- | --- |
| change | The maximum amount of change to the referenced stat. | _integer_ |
| move | The move causing the change. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Move](https://pokeapi.co/docs/v2#move)_) |

#### NatureStatAffectSets (type)

| Name | Description | Type |
| --- | --- | --- |
| increase | A list of natures and how they change the referenced stat. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Nature](https://pokeapi.co/docs/v2#nature))_ |
| decrease | A list of nature sand how they change the referenced stat. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Nature](https://pokeapi.co/docs/v2#nature))_ |

### Types (endpoint)

Types are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

GET https://pokeapi.co/api/v2/type/{id or name}/

- id:5
- name:"ground"
- ▶


damage\_relations:{} 6 keys
- ▶


past\_damage\_relations:\[\] 1 item
  - ▶


    0:{} 2 keys
    - ▶


      generation:{} 2 keys
      - name:"generation-v"
      - url:"https://pokeapi.co/api/v2/generation/5/"
    - ▶


      damage\_relations:{} 6 keys
- ▶


game\_indices:\[\] 1 item
  - ▶


    0:{} 2 keys
    - game\_index:4
    - ▶


      generation:{} 2 keys
      - name:"generation-i"
      - url:"https://pokeapi.co/api/v2/generation/1/"
- ▶


generation:{} 2 keys
  - name:"generation-i"
  - url:"https://pokeapi.co/api/v2/generation/1/"
- ▶


move\_damage\_class:{} 2 keys
  - name:"physical"
  - url:"https://pokeapi.co/api/v2/move-damage-class/2/"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"ã˜ã‚ã‚“"
    - ▶


      language:{} 2 keys
      - name:"ja"
      - url:"https://pokeapi.co/api/v2/language/1/"
- ▶


pokemon:\[\] 1 item
  - ▶


    0:{} 2 keys
    - slot:1
    - ▶


      pokemon:{} 2 keys
      - name:"sandshrew"
      - url:"https://pokeapi.co/api/v2/pokemon/27/"
- ▶


moves:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"sand-attack"
    - url:"https://pokeapi.co/api/v2/move/28/"

View raw JSON (2.743 kB, 129 lines)

#### Type (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| damage\_relations | A detail of how effective this type is toward others and vice versa. | [TypeRelations](https://pokeapi.co/docs/v2#typerelations) |
| past\_damage\_relations | A list of details of how effective this type was toward others and vice versa in previous generations | list _[TypeRelationsPast](https://pokeapi.co/docs/v2#typerelationspast) ([Type](https://pokeapi.co/docs/v2#type))_ |
| game\_indices | A list of game indices relevent to this item by generation. | list _[GenerationGameIndex](https://pokeapi.co/docs/v2#generationgameindex)_ |
| generation | The generation this type was introduced in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| move\_damage\_class | The class of damage inflicted by this type. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[MoveDamageClass](https://pokeapi.co/docs/v2#movedamageclass)_) |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |
| pokemon | A list of details of Pokémon that have this type. | list _[TypePokemon](https://pokeapi.co/docs/v2#typepokemon)_ |
| moves | A list of moves that have this type. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Move](https://pokeapi.co/docs/v2#move))_ |

#### TypePokemon (type)

| Name | Description | Type |
| --- | --- | --- |
| slot | The order the Pokémon's types are listed in. | _integer_ |
| pokemon | The Pokémon that has the referenced type. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Pokemon](https://pokeapi.co/docs/v2#pokemon)_) |

#### TypeRelations (type)

| Name | Description | Type |
| --- | --- | --- |
| no\_damage\_to | A list of types this type has no effect on. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| half\_damage\_to | A list of types this type is not very effect against. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| double\_damage\_to | A list of types this type is very effect against. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| no\_damage\_from | A list of types that have no effect on this type. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| half\_damage\_from | A list of types that are not very effective against this type. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |
| double\_damage\_from | A list of types that are very effective against this type. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([Type](https://pokeapi.co/docs/v2#type))_ |

#### TypeRelationsPast (type)

| Name | Description | Type |
| --- | --- | --- |
| generation | The last generation in which the referenced type had the listed damage relations | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |
| damage\_relations | The damage relations the referenced type had up to and including the listed generation | [TypeRelations](https://pokeapi.co/docs/v2#typerelations) |

## Utility (group)

### Languages (endpoint)

Languages for translations of API resource information.

GET https://pokeapi.co/api/v2/language/{id or name}/

- id:1
- name:"ja"
- official:true
- iso639:"ja"
- iso3166:"jp"
- ▶


names:\[\] 1 item
  - ▶


    0:{} 2 keys
    - name:"Japanese"
    - ▶


      language:{} 2 keys
      - name:"en"
      - url:"https://pokeapi.co/api/v2/language/9/"

View raw JSON (0.247 kB, 16 lines)

#### Language (type)

| Name | Description | Type |
| --- | --- | --- |
| id | The identifier for this resource. | _integer_ |
| name | The name for this resource. | _string_ |
| official | Whether or not the games are published in this language. | _boolean_ |
| iso639 | The two-letter code of the country where this language is spoken. Note that it is not unique. | _string_ |
| iso3166 | The two-letter code of the language. Note that it is not unique. | _string_ |
| names | The name of this resource listed in different languages. | list _[Name](https://pokeapi.co/docs/v2#name)_ |

### Common Models

#### APIResource (type)

| Name | Description | Type |
| --- | --- | --- |
| url | The URL of the referenced resource. | _string_ |

#### Description (type)

| Name | Description | Type |
| --- | --- | --- |
| description | The localized description for an API resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

#### Effect (type)

| Name | Description | Type |
| --- | --- | --- |
| effect | The localized effect text for an API resource in a specific language. | _string_ |
| language | The language this effect is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

#### Encounter (type)

| Name | Description | Type |
| --- | --- | --- |
| min\_level | The lowest level the Pokémon could be encountered at. | _integer_ |
| max\_level | The highest level the Pokémon could be encountered at. | _integer_ |
| condition\_values | A list of condition values that must be in effect for this encounter to occur. | list _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource) ([EncounterConditionValue](https://pokeapi.co/docs/v2#encounterconditionvalue))_ |
| chance | Percent chance that this encounter will occur. | _integer_ |
| method | The method by which this encounter happens. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[EncounterMethod](https://pokeapi.co/docs/v2#encountermethod)_) |

#### FlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| flavor\_text | The localized flavor text for an API resource in a specific language. Note that this text is left unprocessed as it is found in game files. This means that it contains special characters that one might want to replace with their visible decodable version. Please check out this [issue](https://github.com/veekun/pokedex/issues/218#issuecomment-339841781) to find out more. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |
| version | The game version this flavor text is extracted from. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |

#### GenerationGameIndex (type)

| Name | Description | Type |
| --- | --- | --- |
| game\_index | The internal id of an API resource within game data. | _integer_ |
| generation | The generation relevent to this game index. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Generation](https://pokeapi.co/docs/v2#generation)_) |

#### MachineVersionDetail (type)

| Name | Description | Type |
| --- | --- | --- |
| machine | The machine that teaches a move from an item. | _[APIResource](https://pokeapi.co/docs/v2#apiresource)_ ( _[Machine](https://pokeapi.co/docs/v2#machine)_) |
| version\_group | The version group of this specific machine. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

#### Name (type)

| Name | Description | Type |
| --- | --- | --- |
| name | The localized name for an API resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

#### NamedAPIResource (type)

| Name | Description | Type |
| --- | --- | --- |
| name | The name of the referenced resource. | _string_ |
| url | The URL of the referenced resource. | _string_ |

#### VerboseEffect (type)

| Name | Description | Type |
| --- | --- | --- |
| effect | The localized effect text for an API resource in a specific language. | _string_ |
| short\_effect | The localized effect text in brief. | _string_ |
| language | The language this effect is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |

#### VersionEncounterDetail (type)

| Name | Description | Type |
| --- | --- | --- |
| version | The game version this encounter happens in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |
| max\_chance | The total percentage of all encounter potential. | _integer_ |
| encounter\_details | A list of encounters and their specifics. | list _[Encounter](https://pokeapi.co/docs/v2#encounter)_ |

#### VersionGameIndex (type)

| Name | Description | Type |
| --- | --- | --- |
| game\_index | The internal id of an API resource within game data. | _integer_ |
| version | The version relevent to this game index. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Version](https://pokeapi.co/docs/v2#version)_) |

#### VersionGroupFlavorText (type)

| Name | Description | Type |
| --- | --- | --- |
| text | The localized name for an API resource in a specific language. | _string_ |
| language | The language this name is in. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[Language](https://pokeapi.co/docs/v2#language)_) |
| version\_group | The version group which uses this flavor text. | _[NamedAPIResource](https://pokeapi.co/docs/v2#namedapiresource)_ ( _[VersionGroup](https://pokeapi.co/docs/v2#versiongroup)_) |

Created by [Paul Hallett](https://github.com/phalt) and other [PokéAPI contributors](https://github.com/PokeAPI/pokeapi/graphs/contributors) around the world. Pokémon and Pokémon character names are trademarks of Nintendo.

[![Status](https://img.shields.io/badge/dynamic/json?color=blue&label=status&query=%24.status.description&url=https%3A%2F%2Fzlfyqp3hlvly.statuspage.io%2Fapi%2Fv2%2Fsummary.json)](https://pokeapi.statuspage.io/)