   M S B A M L   `   `   `  ����F  BDatabinding, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null)clr-namespace:DatabindingDatabinding  5   	       Databinding.MainWindow   5   	   W SPresentationCore, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   +localclr-namespace:Databinding     5   	     � Title$  
MainWindow��5   	   $	��450��6   $	��800��6)    � 	Resources 5	        Databinding.TextToBool   myconverter��%   &	          5
   
   61   5      .��5      � .+�5   
   �� -   5        $��source��5      $
��Left=�6    $��
163,71,0,0q�6;    �� TextWrapping$
 Wrap=�6O   $	��Top=�6d   $	��120��6|   $��20(�6�   �� 5   
   -   5        $��destination��5   |   $
��Left=�6�   $��163,161,0,0q�6�   $
 Wrap=�6�   $	��Top=�6�   $	��120��6�   $��20(�6�   ��6   ��  �� ElementName$ source�� �� Path$
 Text� �� Mode$ OneWayToSource=� �� UpdateSourceTrigger$ PropertyChanged=�6�   �� 5   
   -   5        $��S1��5      $
��Left=�6   $��
484,85,0,0q�67   $	��Top=�6K   $	��120��6c   �� 5   
   -   5        $��T3��5   w   $
��Left=�6�   $��484,161,0,0q�6�   $
 Wrap=�6�   $	��Top=�6�   $	��120��6�   $��20(�6�   ��6   �� $ S1��$ Value�$ OneWayToSource=�$ PropertyChanged=�6�   �� 5   
   -   5        $��	T4_source��5      $
��Left=�6#   $��326,255,0,0q�6>   $
 Wrap=�6S   $	��Top=�6g   $	��120��6   $��20(�6�   �� 5   
   -   5        $��Check1��5   r   $��CheckBox��6�   $
��Left=�6�   $��473,262,0,0q�6�   $	��Top=�6�    d� 	IsChecked 6   �� $ 	T4_source��$
 Text� �� 	Converter# [  6�   5      5      