## **System Base**

This system is heavily built on the foundation of another system:
https://github.com/KaxuTheSheep/ttrpgplayer

---
## **Stats**

| **Stat** |   **Formula**   |
| :------: | :-------------: |
|  Vigor   | RACE + Vitality |
|  Aether  | RACE + Insight  |
| Evasion  |    8 + Grace    |

---
## **Movement**

There are three different types of movement: Fast, Standard and Slow. These are shown below:

### **Standard:**

| Movement Type | Priority |       Travel rate per tick       | Action Type |
| :-----------: | :------: | :------------------------------: | :---------: |
|     Walk      |    10    |                3m                |    Free     |
|      Run      |    8     |                8m                |    Full     |
|     Climb     |    5     |               1.5m               |    Free     |
|     Swim      |    4     |               1.5m               |    Free     |
|    Burrow     |    2     |               0.5m               |    Free     |
|     Crawl     |    7     |                1m                |    Free     |
|     Jump      |    8     | 1.5( + Might)m<br>1 meter height |    Half     |
### **Fast:**

| Movement Type | Priority |      Travel rate per tick      | Action Type |
| :-----------: | :------: | :----------------------------: | :---------: |
|     Walk      |    12    |               4m               |    Free     |
|      Run      |    10    |              10m               |    Full     |
|     Climb     |    8     |               2m               |    Free     |
|     Swim      |    6     |               2m               |    Free     |
|    Burrow     |    3     |               1m               |    Free     |
|     Crawl     |    8     |              1.5m              |    Free     |
|     Jump      |    10    | 2( + Grace)m<br>1 meter height |    Half     |
### **Slow:**

| Movement Type | Priority |       Travel rate per tick       | Action Type |
| :-----------: | :------: | :------------------------------: | :---------: |
|     Walk      |    9     |                3m                |    Free     |
|      Run      |    7     |                7m                |    Full     |
|     Climb     |    4     |                1m                |    Free     |
|     Swim      |    3     |               1.5m               |    Free     |
|    Burrow     |    2     |               0.5m               |    Free     |
|     Crawl     |    6     |               0.5m               |    Free     |
|     Jump      |    7     | 1( + Might)m<br>0.5 meter height |    Half     |

---
## **Languages**

All races know common, and most know an extra language too. Ashen ones may pick from any of the languages available. Below is a list of all the languages.

- Common
- Runic
- Latin
- Draconic
- Cipher

---
## **Estus**

**Each player starts with 2 estus flasks. These can be allocated in any chosen way between crimson estus flasks and cerulean estus flasks.**
**The former restores vigor and the latter restores aether.**
  
**These can be upgraded throughout your adventures with estus shards to increase the capacity held, or undead bone shards to increase the amount restored when used.**

| **Flask Level** | **Amount Restored** |
| :-------------: | :-----------------: |
|      base       |          7          |
|       +1        |         11          |
|       +2        |         15          |
|       +3        |         20          |
|       +4        |         25          |
|       +5        |         30          |
|       +6        |         34          |
|       +7        |         36          |


---
## **Levels**  

**When defeating enemies, you will acquire a resource called “souls”. These souls can be exchanged for trait points or used as currency in shops, or even changed into consumable item variants of souls.

**Carrying souls is a risky choice, as if you enter a dying state, all souls on you will be lost permanently, apart from item souls.

**These trait points can be exchanged for and used at kindled bonfires.

**Levels are awarded by using a “shard of a great soul” at a kindled bonfire, and each level grants an overall buff to ones self, along with a few trait points that can be allocated freely.

**These shards can be found by slaying renowned enemies named “shard bearers”, the great beasts that rule the ruined lands of Yarven.

**Each level acquired will increase the following stats by:  
Vigor: 1d10 + vitality  
Aether: 1d6 + insight

---
## **Unique Items**

|        **Name**        |                                   **Use**                                   |                 **Stat Cost**                  |
| :--------------------: | :-------------------------------------------------------------------------: | :--------------------------------------------: |
|          Soul          |             Can be used to acquire souls. Not lost upon “death”             |                      N/A                       |
|         Staff          |                        Used to cast only sorceries.                         |  Equal to aether cost of spell being casted.   |
|          Seal          |                       Used to cast only incantations.                       |  Equal to aether cost of incant being casted.  |
|  Spirit Calling Bell   |                        Used to summon spirit ashes.                         | Equal to aether cost of spirit being summoned. |
|      Memory Stone      | Allows the wearer to gain an additional attunement slot. Can wear multiple. |                      N/A                       |
|    Starlight Shards    |               Use to regain lost aether, restores 10 aether.                |                      N/A                       |
|     Stonesword Key     |       Used as a consumable key to open certain locked doors or seals.       |                      N/A                       |
|         Ember          |             Increases max vigor by 20% until you become downed.             |                      N/A                       |
|     Warming Stones     |   Places down a stone that heals 4 vigor per turn for 3 turns. 2m radius.   |                      N/A                       |
|    Divine Blessing     |         Fully restores vigor and cures all current status build up.         |                      N/A                       |
|    Hidden Blessing     |                           Fully restores aether.                            |                      N/A                       |
|    Smithing Stones     |            Increase the level of your standard weapon up to +25.            |                      N/A                       |
| Somber Smithing Stones |             Increase the level of your unique weapon up to +10.             |                      N/A                       |
|    Ghost Glovewort     |          Increase the level of your usable spirit ashes up to +10.          |                      N/A                       |

---
## **Status Build Up**

There are 7 status effects in the game to be wary about. Everyone will have a resistance bar for each effect, and when the build up reaches your max resistance, you will suffer the effect of the status you have been afflicted by.

|  **Name**   |                                                       **Result**                                                        |
| :---------: | :---------------------------------------------------------------------------------------------------------------------: |
|    Bleed    |                                     Take damage equal to 15% of your maximum vigor.                                     |
|  Frostbite  | Take damage equal to 10% of your maximum vigor and temporarily reduce your evasion by 2 for "vitality" amount of turns. |
|    Sleep    |                                             Used to cast only incantations.                                             |
|   Poison    |                                              Used to summon spirit ashes.                                               |
| Scarlet Rot |                       Allows the wearer to gain an additional attunement slot. Can wear multiple.                       |
|   Madness   |                                     Use to regain lost aether, restores 10 aether.                                      |
| Deathblight |                             Used as a consumable key to open certain locked doors or seals.                             |
