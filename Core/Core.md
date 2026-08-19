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

**Each player starts with 3 estus flasks. These can be allocated in any chosen way between crimson estus flasks and cerulean estus flasks.**
**The former restores vigor and the latter restores aether.**
  
**These can be upgraded throughout your adventures with estus shards to increase the capacity held, or undead bone shards to increase the amount restored when used.**

| **Flask Level** | **Amount Restored** |
| :-------------: | :-----------------: |
|      base       |          9          |
|       +1        |         13          |
|       +2        |         17          |
|       +3        |         22          |
|       +4        |         27          |
|       +5        |         32          |
|       +6        |         36          |
|       +7        |         38          |


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

|         **Name**         |                                   **Use**                                   |                 **Stat Cost**                  |
| :----------------------: | :-------------------------------------------------------------------------: | :--------------------------------------------: |
|           Soul           |             Can be used to acquire souls. Not lost upon “death”             |                      N/A                       |
|          Staff           |                        Used to cast only sorceries.                         |  Equal to aether cost of spell being casted.   |
|           Seal           |                       Used to cast only incantations.                       |  Equal to aether cost of incant being casted.  |
|   Spirit Calling Bell    |                        Used to summon spirit ashes.                         | Equal to aether cost of spirit being summoned. |
|       Memory Stone       | Allows the wearer to gain an additional attunement slot. Can wear multiple. |                      N/A                       |
|     Starlight Shards     |               Use to regain lost aether, restores 10 aether.                |                      N/A                       |
|      Stonesword Key      |       Used as a consumable key to open certain locked doors or seals.       |                      N/A                       |
|          Ember           |             Increases max vigor by 20% until you become downed.             |                      N/A                       |
|      Warming Stones      |   Places down a stone that heals 4 vigor per turn for 3 turns. 2m radius.   |                      N/A                       |
|     Divine Blessing      |         Fully restores vigor and cures all current status build up.         |                      N/A                       |
|     Hidden Blessing      |                           Fully restores aether.                            |                      N/A                       |
|     Smithing Stones      |            Increase the level of your standard weapon up to +25.            |                      N/A                       |
|  Somber Smithing Stones  |             Increase the level of your unique weapon up to +10.             |                      N/A                       |
| Polished Smithing Stones |               Increases the level of an upgradable talisman.                |                      N/A                       |
|     Ghost Glovewort      |          Increase the level of your usable spirit ashes up to +10.          |                      N/A                       |

---
## **Status Build Up**

There are 7 status effects in the game to be wary about. Everyone will have a resistance value for each effect, and when the build up value reaches your resistance value, you will suffer the effect of the status you have been afflicted by. Once you have recovered from this effect, your current build up returns back to 0.

|  **Name**   |                                                                                  **Result**                                                                                  |
| :---------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    Bleed    |                                                               Take damage equal to 15% of your maximum vigor.                                                                |
|  Frostbite  |                                     Take damage equal to 10% of your maximum vigor and temporarily reduce your evasion by 2 for 3 turns.                                     |
|    Sleep    |                                    Reduces your aether by 10% of your max aether and become completely asleep for 2 turns, or until hit.                                     |
|   Poison    | Take damage equal to 5% of your max vigor for 8 turns. This damage is applied the moment you are afflicted by poison, and then again at tick 20 for the following 7 rounds.  |
| Scarlet Rot | Take damage equal to 10% of your max vigor for 8 turns. This damage is applied the moment you are afflicted by poison, and then again at tick 20 for the following 7 rounds. |
|   Madness   |            Take damage equal to 15% of your maximum vigor and reduce your aether by 10% of your max aether. You become briefly stunned for the following 4 ticks.            |
| Deathblight |                                Thorns of pure death sprout from your core, growing outwards and immediately putting you into the dying state.                                |
When afflicting enemies with these effects, they will suffer the same result as you would. However, once recovered from these effects, their resistance to it will double. For example, an enemy with 150 bleed resistance that has been bled will then get 300 bleed resistance. This will repeat until the enemy has been felled.

---
## **Jump Attacks**

By spending a half action to jump before using an attack, you can increase the damage you deal by a further 1d6. 

---
## **Poise**

Everyone will have a poise value, similar to that of status effects. When being hit with certain attacks, typically melee weapons and some incantations, you will recieve poise build up. Once this build up reaches your poise value, you will be stunned for 8 ticks from the tick you got stunned. This applies to enemies as well the same way as it does you.

If you are quick enough and in direct range, you can use a reaction to "Riposte" the enemy, dealing large damage in a single strike. Once a Riposte is carried out, the staggered enemy will no longer be stunned. Moreover, any damage they receive while stunned will half the stagger time to 4, and so on. In short, hitting an enemy twice while they are stunned will let them get back on their feet. 

Below are the values for each Critical Type, of which every weapon will have and will determine the damage done from a Riposte.

| Critical Damage Type | **Damage Dealt of Max Vigor** |
| :------------------: | :---------------------------: |
|         High         |              15%              |
|        Medium        |              10%              |
|         Low          |              5%               |
|    Insignificant     |              2%               |

---
## **Buff Types**

There are two separate types of buffs. These consist of Body buffs, and Aura buffs. Body buffs are applied to only one individual at a time, whereas Aura buffs tend to be applied in an area, effecting everyone in range. One of each type of buff can be applied at the same time, but two different Body buffs cannot be used simultaneously.

---

## **Two-Handing**

When using a weapon, you can choose to two hand. This increases the damage dealt, poise damage dealt, and can also change some other features depending on weapon traits.

The increase to poise damage is by 25%, and the increase to normal damage is the next step up in dice rank. Below is the table for reference, along with the average and range for reasoning.

| **Dice Rank** | **Roll** | **Average** | **Range** |
| :-----------: | :------: | :---------: | :-------: |
|       1       |   1d4    |     2.5     |    1-4    |
|       2       |   1d6    |     3.5     |    1-6    |
|       3       |   1d8    |     4.5     |    1-8    |
|       4       |   2d4    |      5      |    2-8    |
|       5       |   1d10   |     5.5     |   1-10    |
|       6       |   1d12   |     6.5     |   1-12    |
|       7       |   2d6    |      7      |   2-12    |
|       8       |   3d4    |     7.5     |   3-12    |
|       9       |   2d8    |      9      |   2-16    |
|      10       |   3d6    |    10.5     |   3-18    |
|      10       |   1d20   |    10.5     |   1-20    |
|      11       |   2d10   |     11      |   2-20    |
|      12       |   2d12   |     13      |   2-24    |
|      13       |   3d8    |    13.5     |   3-24    |
|      14       |   3d10   |    16.5     |   3-30    |
|      15       |   3d12   |    19.5     |   3-36    |
|      16       |   2d20   |     21      |   2-40    |
|      17       |   3d20   |    31.5     |   3-60    |

