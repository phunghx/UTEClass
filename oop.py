using MagicDestroyers.Enums;
using System;

namespace Baitap3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(MagicDestroyers.PlayersInfo.playersInfoDirectory);
        }
    }
}
namespace MagicDestroyers.Enums 
{
//////////your code here ////////

//////////end your code/////////
}
namespace MagicDestroyers.Equipment.Armors.Leather
{
    public class LightLeatherVest
    {
        private const int DEFAULT_ARMOR_POINTS = 10;

        

        public int ArmorPoints
        {
            get
            {
                return armorPoints;
            }
            set
            {
                if (value >= 0)
                {
                    this.armorPoints = value;
                }
                else
                {
                    throw new ArgumentOutOfRangeException(string.Empty, "Armor Points value should be a positive number");
                }
            }
        }

        public LightLeatherVest()
            : this(DEFAULT_ARMOR_POINTS)
        {
        }
        //////////your code here ////////
        private int armorPoints;
        //////////end your code/////////
        
    }
}

namespace MagicDestroyers.Equipment.Weapons.Sharp
{
    public class Sword
    {
        private const int DEFAULT_DAMAGE_POINTS = 10;

        public int DamagePoints
        {
            get
            {
                return damagePoints;
            }
            set
            {
                if (value >= 0)
                {
                    this.damagePoints = value;
                }
                else
                {
                    throw new ArgumentOutOfRangeException(string.Empty, "Damage Points value should be a positive number");
                }
            }
        }

        public Sword()
            : this(DEFAULT_DAMAGE_POINTS)
        {
        }

        //////////your code here ////////

        //////////end your code/////////
    }
}

namespace MagicDestroyers.Characters.Spellcasters
{
    public class Necromancer
    {
        private const Faction DEFAULT_FACTION = Faction.Spellcaster;
        private const int DEFAULT_LEVEL = 1;
        private const int DEFAULT_HEALTH_POINTS = 120;
        private const int DEFAULT_ABILITY_POINTS = 100;
        private const string DEFAULT_NAME = "Necromus";

        private readonly Equipment.Armors.Leather.LightLeatherVest DEFAULT_BODY_ARMOR = new Equipment.Armors.Leather.LightLeatherVest();
        private readonly Equipment.Weapons.Sharp.Sword DEFAULT_WEAPON = new Equipment.Weapons.Sharp.Sword();

        

        public Faction Faction
        {
            get
            {
                return faction;
            }
            set
            {
                this.faction = value;
            }
        }

        public int AbilityPoints
        {
            get
            {
                return abilityPoints;
            }
            set
            {
                if (value >= 0 && value <= 100)
                {
                    abilityPoints = value;
                }
                else
                {
                    throw new ArgumentOutOfRangeException(string.Empty, "Inappropriate value, the value should be >= 0 and <= 10.");
                }
            }
        }
        public int HealthPoints
        {
            get
            {
                return healthPoints;
            }
            set
            {
                if (value >= 0 && value <= 100)
                {
                    healthPoints = value;
                }
                else
                {
                    throw new ArgumentOutOfRangeException(string.Empty, "Inappropriate value, the value should be >= 0 and <= 100.");
                }
            }
        }
        public int Level
        {
            get
            {
                return level;
            }
            set
            {
                if (value >= 0)
                {
                    healthPoints = value;
                }
                else
                {
                    throw new ArgumentOutOfRangeException(string.Empty, "Inappropriate value, level should always be positive.");
                }
            }
        }

        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                if (value.Length >= 3 && value.Length <= 12)
                {
                    name = value;
                }
                else
                {
                    throw new ArgumentException(string.Empty, "Inappropriate length of name, name should be between 3 and 12 characters.");
                }
            }
        }

        public Equipment.Armors.Leather.LightLeatherVest BodyArmor
        {
            get
            {
                return bodyArmor;
            }
            set
            {
                bodyArmor = value;
            }
        }
        public Equipment.Weapons.Sharp.Sword Weapon
        {
            get
            {
                return weapon;
            }
            set
            {
                weapon = value;
            }
        }

        public Necromancer()
            : this(DEFAULT_NAME, DEFAULT_LEVEL)
        {
        }

        public Necromancer(string name, int level)
            : this(name, level, DEFAULT_HEALTH_POINTS)
        {
        }

        //////////your code here ////////

        //////////end your code/////////

        public void ShadowRage()
        {
            throw new NotImplementedException();
        }

        public void VampireTouch()
        {
            throw new NotImplementedException();
        }

        public void BoneShield()
        {
            throw new NotImplementedException();
        }
    }
}

namespace MagicDestroyers
{
    public static class PlayersInfo
    {
        private static string playersInfoDirectory = "";
        
        
        //////////your code here ////////
        public static void PrintFullInfo()  
        {
              System.Console.WriteLine("C:\home")
        }

        //////////end your code/////////

        
    }
}


