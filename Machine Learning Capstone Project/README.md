# Capstone Project: Price Optimization For New Product (E-commerce)
This project is created for allowing companies to understand the optimized price range of their new products to be uploaded on E-commerce site, so the companies could determine which products have a higher chance to be purchased and set up their marketing strategy efficiently.

## Problem Statement
What is the optimized price range bases on specified categories, original country and other features like weight and size?

## Dataset
Dataset is downloaded from the databank of an E-commerce site , it provides the data of daily sales with below details:

1. membership_level
2. order_date
3. order_time_range
4. card_class	
5. card_issuer
6. card_type	
7. area
8. district	
9. delivery_district	
10. delivery_zone
11. housing_type	
12. order_value	
13. total_discounts	
14. cash_voucher_applied_value	
15. paid_voucher_applied_value
16. product_id	
17. sku_id	
18. primary_sku_id	
19. bundle_set	
20. brand_en	
21. brand_chi	
22. quantity	
23. total_price	
24. primary_category	
25. primary_category_name_en	
26. primary_category_name_chi	
27. sub_cat_1_name_en	
28. sub_cat_1_name_chi	
29. sub_cat_2_name_en	
30. sub_cat_2_name_chi	
31. sub_cat_3_name_en	
32. sub_cat_3_name_chi	
33. sub_cat_4_name_en	
34. sub_cat_4_name_chi	
35. sku_level_promotion_amount	
36. store_level_promotion_amount	
37. mall_level_promotion_amount
38. is_consignment	
39. sku_ready_required_days
40. packing_spec_en	
41. packing_spec_chi	
42. packing_box_type	
43. storage_type	
44. size	
45. weight	
46. height	
47. length	
48. width	
49. manufacturer_country_en	
50. manufacturer_country_chi	

## Data Cleansing
During the process of data cleansing, the columns below have been deleted:

1. order_date (All data are for July 2022, and we could not sell products to the past)
2. order_time_range (No big difference and we cannot control it)
3. card_issuer (Converted to Citibank/ Non-Citibank)
4. district	("area" is already enough for customer targeting)
5. delivery_district	(For internal uses)
6. delivery_zone (Same as district)
7. order_value (Converted to "order_value_from" and "order_value_to)
8. total_discounts (Converted to any_discounts)
9. cash_voucher_applied_value	(Converted to any_vouchers)
10. paid_voucher_applied_value (Converted to any_vouchers)
11. product_id	(Prevent overfitting and undefinable)
12. sku_id	(Undefinable)
13. primary_sku_id	(Undefinable)
14. brand_en	(Undefinable)
15. brand_chi	(Same data in English provided)
16. total_price	(Converted to total_price_range)
17. primary_category	(All in the same value)
18. primary_category_name_en	(All in the same value)
19. primary_category_name_chi	(Same data in English provided)
20. sub_cat_1_name_en	(All in the same value)
21. sub_cat_1_name_chi	(Same data in English provided)
22. sub_cat_2_name_en	(All in the same value)
23. sub_cat_2_name_chi	(Same data in English provided)
24. sub_cat_3_name_en	(All in the same value)
25. sub_cat_3_name_chi	(Same data in English provided)
26. sub_cat_4_name_chi	(Same data in English provided)
27. sku_level_promotion_amount	(Undefinable and cannot control)
28. store_level_promotion_amount	(Converted to "store_promotion")
29. mall_level_promotion_amount (All in the same value)
30. packing_spec_en	 (Hard to classify and "weight" could do the same effect)
31. packing_spec_chi	(Same data in English provided)
32. storage_type	("packing_box_type" could do the same effect while "storage_type" has missing values)
33. size	(All in the same value)
34. manufacturer_country_en	
35. manufacturer_country_chi	(Same data in English provided)

The columns as below have been left as features:

1. membership_level (str)
2. card_type (str)
3. area (str)
4. housing_type (str)
5. bundle_set (int)
6. quantity (int)
7. sub_cat_3_name_enis_consignment (str)
8. sku_ready_required_days (int)
9. packing_box_type (str)
10. weight (int)
11. height (int)
12. length (int)
13. width (int)
14. is_citibank (int)
15. order_value_from (float)
16. order_value_to (float)
17. any_discounts (int)
18. any_vouchers (int)
19. store_promotion (int)
20. total_price_range (str) (The one targeted to be predicted)
