using Magic[MSSV].Equipment.Armors.Heavy;
using Magic[MSSV].Equipment.Armors.Leather;
using Magic[MSSV].Equipment.Armors.Light;
using Magic[MSSV].Equipment.Weapons.Blunt;
using Magic[MSSV].Equipment.Weapons.Sharp;
using System;

namespace Ex2[MSSV]
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Magic[MSSV].Characters.Melee.Knight knight = new Magic[MSSV].Characters.Melee.Knight();
            try
            {
                knight.AbilityPoints = 10; 
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            try
            {
                knight.Faction = "Melee";
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(ex.Message);
            }
            try
            {
                knight.Name = "Knight";
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(ex.Message);
            }
            try
            {
                knight.Level = 10;
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            try
            {
                knight.HealthPoints = 50;
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            Chainlink knightChainlink = new Chainlink();
            try { 
                knightChainlink.ArmorPoints = 10;
            }
            catch(ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            knight.BodyArmor = knightChainlink;
            Hammer knightHammer = new Hammer();
            try
            {
                knightHammer.Damage = 1;
            }
            catch(ArgumentOutOfRangeException ex)
            {
                Console.WriteLine(ex.Message);
            }
            knight.Weapon = knightHammer;

            try
            {
                knight.HolyBlow();
            }
            catch(NotImplementedException ex)
            {
                Console.WriteLine("Not Implement");
            }
            try
            {
                knight.PurifySoul();
            }
            catch (NotImplementedException ex)
            {
                Console.WriteLine("Not Implement");
            }
            try
            {
                knight.RighteousWings();
            }
            catch (NotImplementedException ex)
            {
                Console.WriteLine("Not Implement");
            }
            
        }
    }
}

//////////your code here ////////

//////////end your code/////////
