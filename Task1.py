{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNw0OdKFV5tOb3WUloli3PV",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Harsh-20422/Intenship/blob/master/Task1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6W4xBt4WNBXr",
        "outputId": "43c4db60-0415-45dd-a826-ad88ff402219"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "updated set: {1, 4, 5, 6, 7, 10}\n"
          ]
        }
      ],
      "source": [
        "my_set={1,2,3,4,5,6}\n",
        "my_set.add(7)\n",
        "my_set.remove(3)\n",
        "my_set.discard(2)\n",
        "my_set.add(10)\n",
        "print('updated set:',my_set)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_list=[1, 2, 3, 4, 5, 6]\n",
        "my_list.append(7)\n",
        "my_list.remove(5)\n",
        "my_list[0]\n",
        "print(my_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6awE2tK4NEq2",
        "outputId": "d8397d89-95b6-4265-9a9d-3c0a1e8dc7a0"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_dict={'name':'harsh','age':'19', 'city': 'banglore'}\n",
        "my_dict['gender']='male'\n",
        "del my_dict['age']\n",
        "my_dict['city']='Goa'\n",
        "print('updated dictionary:',my_dict)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zR3Oyy0BNOIw",
        "outputId": "74d67279-a603-4e1c-f407-58c03636e656"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "updated dictionary: {'name': 'harsh', 'city': 'Goa', 'gender': 'male'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Tn7orpYNNRni"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}